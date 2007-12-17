%define version 0.1.20060928
%define release %mkrel 3
%define epoch 1

Summary:	Unified Chinese True Type font
Name:		fonts-ttf-chinese
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}

Source6:	cidinst.chinese
Source7:	cidunin.chinese
Source10:	http://apt.debian.org.tw/pool/t/ttf-arphic-ukai/ttf-arphic-ukai_%{version}.orig.tar.gz
Source11:	http://apt.debian.org.tw/pool/t/ttf-arphic-ukai/ttf-arphic-uming_%{version}.orig.tar.gz

URL:		http://www.freedesktop.org/wiki/Software/CJKUnifonts
License:	Arphic Public License
Group:		System/Fonts/True type
BuildArch:	noarch
Requires(post): fontconfig
Requires(postun): fontconfig
Obsoletes:	fonts-ttf-big5
Provides:	fonts-ttf-big5 = %{epoch}:%{version}-%{release}
Obsoletes:	fonts-ttf-gb2312
Provides:	fonts-ttf-gb2312 = %{epoch}:%{version}-%{release}

%description
Chinese True Type font covering both tranditional and simplified chinese,
in Sung and Kai font face. It was merged by Arne Goetje, using Sung/Kai
face fonts (both in trad. and simp. Chinese) donated by Arphic Technology
Co Ltd.

In addition, it includes embedded 11-16 pixel bitmap fonts done by Firefly,
and HKSCS(Hong Kong) glyphs done by Akar et. al.

%prep
%setup -q -c -T -n fonts-ttf-chinese -a 10 -a 11
 
%build
mkdir doc
# prevent name clash
cp ttf-arphic-ukai-%{version}/README doc/README-ukai
cp ttf-arphic-uming-%{version}/README doc/README-uming
cp ttf-arphic-ukai-%{version}/CONTRIBUTERS ttf-arphic-ukai-%{version}/*.xdelta ttf-arphic-uming-%{version}/*.xdelta doc/

# merge fonts.dir
grep uming.ttf ttf-arphic-uming-%{version}/fonts.dir > fonts.dir.prepare
grep ukai.ttf ttf-arphic-ukai-%{version}/fonts.dir >> fonts.dir.prepare
wc -l fonts.dir.prepare |awk -F' ' '{print $1}' > fonts.dir
cat fonts.dir.prepare >> fonts.dir

# merge fonts.scale
grep uming.ttf ttf-arphic-uming-%{version}/fonts.scale > fonts.scale.prepare
grep ukai.ttf ttf-arphic-ukai-%{version}/fonts.scale >> fonts.scale.prepare
wc -l fonts.scale.prepare |awk -F' ' '{print $1}' > fonts.scale
cat fonts.scale.prepare >> fonts.scale

%install
rm -fr %{buildroot}

install -d %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-ukai-%{version}/ukai.ttf %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-uming-%{version}/uming.ttf %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 fonts.dir fonts.scale %{buildroot}/%{_datadir}/fonts/TTF/chinese/

# merge fonts.alias
cat ttf-arphic-ukai-%{version}/fonts.alias ttf-arphic-uming-%{version}/fonts.alias > %{buildroot}%{_datadir}/fonts/TTF/chinese/fonts.alias

touch %{buildroot}%{_datadir}/fonts/TTF/chinese/fonts.*

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/chinese \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-chinese:pri=50


%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc doc/*
%dir %{_datadir}/fonts/TTF/chinese/
%{_datadir}/fonts/TTF/chinese/*
%{_sysconfdir}/X11/fontpath.d/ttf-chinese:pri=50
