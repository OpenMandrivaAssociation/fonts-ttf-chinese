Summary:	Unified Chinese True Type font
Name:		fonts-ttf-chinese
Epoch:		1
Version:	0.2.20080216.1
Release:	11
License:	Arphic Public License
Group:		System/Fonts/True type
Url:		http://www.freedesktop.org/wiki/Software/CJKUnifonts
Source6:	cidinst.chinese
Source7:	cidunin.chinese
Source10:	http://apt.debian.org.tw/pool/t/ttf-arphic-ukai/ttf-arphic-ukai_%{version}.orig.tar.gz
Source11:	http://apt.debian.org.tw/pool/t/ttf-arphic-ukai/ttf-arphic-uming_%{version}.orig.tar.gz

BuildArch:	noarch
BuildRequires:	fontconfig

%description
Chinese True Type font covering both tranditional and simplified chinese,
in Sung and Kai font face. It was merged by Arne Goetje, using Sung/Kai
face fonts (both in trad. and simp. Chinese) donated by Arphic Technology
Co Ltd.

In addition, it includes embedded 11-16 pixel bitmap fonts done by Firefly,
and HKSCS(Hong Kong) glyphs done by Akar et. al.

%prep
%setup -q -c -T -n ttf-arphic-ukai -a 10
%setup -q -c -T -D -n ttf-arphic-uming -a 11
 
%build
cd ..

mkdir doc -p
# prevent name clash
cp ttf-arphic-ukai/README doc/README-ukai
cp ttf-arphic-uming/README doc/README-uming
cp ttf-arphic-ukai/FONTLOG doc/FONTLOG-ukai
cp ttf-arphic-uming/FONTLOG doc/FONTLOG-uming

cp ttf-arphic-ukai/CONTRIBUTERS ttf-arphic-ukai/KNOWN_ISSUES ttf-arphic-ukai/NEWS ttf-arphic-ukai/TODO doc/

# merge fonts.dir
grep uming.ttc ttf-arphic-uming/fonts.dir > fonts.dir.prepare
grep ukai.ttc ttf-arphic-ukai/fonts.dir >> fonts.dir.prepare
wc -l fonts.dir.prepare |awk -F' ' '{print $1}' > fonts.dir
cat fonts.dir.prepare >> fonts.dir

# merge fonts.scale
grep uming.ttc ttf-arphic-uming/fonts.scale > fonts.scale.prepare
grep ukai.ttc ttf-arphic-ukai/fonts.scale >> fonts.scale.prepare
wc -l fonts.scale.prepare |awk -F' ' '{print $1}' > fonts.scale
cat fonts.scale.prepare >> fonts.scale

%install
cd ..

install -d %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-ukai/ukai.ttc %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-uming/uming.ttc %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 fonts.dir fonts.scale %{buildroot}/%{_datadir}/fonts/TTF/chinese/

mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d/
install -m 644 ttf-arphic-ukai/35-ttf-arphic-ukai-aliases.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/
install -m 644 ttf-arphic-uming/35-ttf-arphic-uming-aliases.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/

touch %{buildroot}%{_datadir}/fonts/TTF/chinese/fonts.*

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/chinese \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-chinese:pri=50

%files
%doc ../doc/*
%dir %{_datadir}/fonts/TTF/chinese/
%{_datadir}/fonts/TTF/chinese/*
%{_sysconfdir}/X11/fontpath.d/ttf-chinese:pri=50
%{_sysconfdir}/fonts/conf.d/*.conf

