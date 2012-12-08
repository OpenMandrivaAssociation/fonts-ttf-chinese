%define version 0.2.20080216.1
%define release %mkrel 10
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
BuildRequires: fontconfig
BuildRoot:	%{_tmppath}/%name-%version-%release-root
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
rm -fr %{buildroot}
cd ..

install -d %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-ukai/ukai.ttc %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 ttf-arphic-uming/uming.ttc %{buildroot}/%{_datadir}/fonts/TTF/chinese/
install -m 644 fonts.dir fonts.scale %{buildroot}/%{_datadir}/fonts/TTF/chinese/

mkdir -p %buildroot%_sysconfdir/fonts/conf.d/
install -m 644 ttf-arphic-ukai/35-ttf-arphic-ukai-aliases.conf %buildroot%_sysconfdir/fonts/conf.d/
install -m 644 ttf-arphic-uming/35-ttf-arphic-uming-aliases.conf %buildroot%_sysconfdir/fonts/conf.d/

touch %{buildroot}%{_datadir}/fonts/TTF/chinese/fonts.*

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/chinese \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-chinese:pri=50


%clean
rm -fr %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ../doc/*
%dir %{_datadir}/fonts/TTF/chinese/
%{_datadir}/fonts/TTF/chinese/*
%{_sysconfdir}/X11/fontpath.d/ttf-chinese:pri=50
%_sysconfdir/fonts/conf.d/*.conf


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1:0.2.20080216.1-10mdv2011.0
+ Revision: 675412
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1:0.2.20080216.1-9
+ Revision: 675176
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.20080216.1-8
+ Revision: 664325
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.20080216.1-7mdv2011.0
+ Revision: 605192
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:0.2.20080216.1-6mdv2010.1
+ Revision: 494132
- fc-cache is now called by an rpm filetrigger

* Wed Nov 11 2009 Funda Wang <fwang@mandriva.org> 1:0.2.20080216.1-5mdv2010.1
+ Revision: 464572
- drop uming bitmap spec

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 1:0.2.20080216.1-4mdv2009.1
+ Revision: 336870
- rebuild

* Fri Sep 26 2008 Funda Wang <fwang@mandriva.org> 1:0.2.20080216.1-3mdv2009.0
+ Revision: 288504
- disable anti-alias for smap pixels

* Sat Jul 12 2008 Funda Wang <fwang@mandriva.org> 1:0.2.20080216.1-2mdv2009.0
+ Revision: 234179
- Provides font alias name for compatibility

* Mon Apr 21 2008 Funda Wang <fwang@mandriva.org> 1:0.2.20080216.1-1mdv2009.0
+ Revision: 196320
- New version 0.2.20080216.1
- fix url

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 1:0.1.20060928-3mdv2008.1
+ Revision: 97967
- use fonts.dir and fonts.scale shipped by upstream, as
  current mkfontdir and mkfontscale is broken for Chinese.

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1:0.1.20060928-2mdv2008.0
+ Revision: 48739
- fontpath.d conversion (#31756)
- minor cleanups

* Sun Apr 29 2007 Funda Wang <fwang@mandriva.org> 1:0.1.20060928-1mdv2008.0
+ Revision: 19111
- 2006 is not supported.
- Corrected version for fonts-ttf-chinese.


* Tue Nov 21 2006 Pablo Saratxaga <pablo@mandriva.com> 0.1-0.20060928.1mdv2007.0
+ Revision: 85822
- new version
- new version (that fixes bug #22614)
- moved to /usr/share/fonts/TTF
- Import fonts-ttf-chinese

* Sat Sep 02 2006 Funda Wang <fundawang@gmail.com> 1:0.1-0.20060903.1mdv2007.0
- New snapshot on 20050903

* Sat Sep 02 2006 Funda Wang <fundawang@gmail.com> 1:0.1-0.20060513.3mdv2007.0
- Rebuild to upload new file

* Mon Jun 05 2006 Funda Wang <fundawang@gmail.com> 1:0.1-0.20060513.2mdv2007.0
- Get rid of the bad symbolic link

* Mon Jun 05 2006 Funda Wang <fundawang@gmail.com> 1:0.1-0.20060513.1mdv2007.0
- New snapshot on 20050513

* Thu Feb 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.1-0.20051009.3mdk
- Fix fc-cache call

* Thu Feb 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.1-0.20051009.2mdk
- Never ship fonts.cache-2

* Wed Nov 09 2005 Abel Cheung <deaddog@mandriva.org> 1:0.1-0.20051009.1mdk
- Drop old arphic fonts, merge in Arne's unified fonts
- Don't execute any ghostscript stuff, because all scripts are useless

* Sun Apr 17 2005 Abel Cheung <deaddog@mandriva.org> 1.3.0-1mdk
- New release 1.3.0

* Sat Feb 19 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.6-2mdk
- moved _datadir/fonts/zh_TW symlink to fonts-ttf-chinese package
  where it belongs (bug #13508),
- made fonts-ttf-big5 and fonts-ttf-gb2312 require fonts-ttf-chinese,
  so an update will install fonts-ttf-chinese

* Sun Feb 13 2005 Abel Cheung <deaddog@mandrake.org> 1.2.6-1mdk
- Firefly font version 1.2.6
- Mark fontconfig cache files as ghost
- Remove icons -- they should be useless now
- Tidying up description, license etc

* Wed Jan 19 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.0-2mdk
- fixed cdi install scripts (the ghostscript script has directory
  paths hardcoded)

* Fri Jan 07 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.0-1mdk
- new version

* Sun Oct 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-21mdk
- added to CID scripts the real postscript names of the ttf fonts

