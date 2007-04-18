%define version 0.1.20060928
%define release %mkrel 1
%define epoch 1


Summary:	Unified Chinese True Type font
Name:		fonts-ttf-chinese
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}

#Source0:	ftp://linux.tmtc.edu.tw/pub/arphic/fonts-ttf-chinese.tar.bz2
#Source1:	cidinst.gb2312
#Source2:	cidunin.gb2312
#Source3:	cidinst.big5
#Source4:	cidunin.big5
#Source5:	http://www.study-area.org/apt/firefly-font/fireflysung-1.3.0.tar.bz2
Source6:	cidinst.chinese
Source7:	cidunin.chinese
Source10:	http://apt.debian.org.tw/pool/t/ttf-arphic-ukai/ttf-arphic-ukai_%{version}.orig.tar.gz
Source11:	http://apt.debian.org.tw/pool/t/ttf-arphic-ukai/ttf-arphic-uming_%{version}.orig.tar.gz

URL:		http://www.freedesktop.org/wiki/Software_2fCJKUnifonts
License:	Arphic Public License
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%name-%version-%release-root
Requires(post): chkfontpath, mkfontdir, mkfontscale, fontconfig
Requires(postun): chkfontpath, mkfontdir, mkfontscale, fontconfig
Obsoletes:	fonts-ttf-big5
Provides:	fonts-ttf-big5 = %{epoch}:%{version}-%{release}
Obsoletes:	fonts-ttf-gb2312
Provides:	fonts-ttf-gb2312 = %{epoch}:%{version}-%{release}
# pull in old fonts, for compatilibity
# FW: This is not needed for Mandriva 2007
# Requires:	fonts-ttf-chinese-compat

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

%install
rm -fr %{buildroot}

install -d %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-ukai-%{version}/ukai.ttf %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-uming-%{version}/uming.ttf %{buildroot}/%{_datadir}/fonts/TTF/chinese/

# merge fonts.alias
cat ttf-arphic-ukai-%{version}/fonts.alias ttf-arphic-uming-%{version}/fonts.alias > %{buildroot}%{_datadir}/fonts/TTF/chinese/fonts.alias

# ghost files
%if %mdkversion <= 200600
touch %{buildroot}%{_datadir}/fonts/TTF/chinese/fonts.cache-1
%endif
touch %{buildroot}%{_datadir}/fonts/TTF/chinese/fonts.alias

%post
[ -x %{_sbindir}/chkfontpath ] && %{_sbindir}/chkfontpath -q -a %{_datadir}/fonts/TTF/chinese
[ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/TTF/chinese
[ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/TTF/chinese
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_sbindir}/chkfontpath ] && %{_sbindir}/chkfontpath -q -r %{_datadir}/fonts/TTF/chinese
  [ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/TTF/chinese
  [ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/TTF/chinese
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc doc/*
%dir %{_datadir}/fonts/
%dir %{_datadir}/fonts/TTF/
%dir %{_datadir}/fonts/TTF/chinese/
%{_datadir}/fonts/TTF/chinese/*.ttf
%{_datadir}/fonts/TTF/chinese/fonts.alias
%if %mdkversion <= 200600
%ghost %{_datadir}/fonts/TTF/chinese/fonts.cache-1
%endif


