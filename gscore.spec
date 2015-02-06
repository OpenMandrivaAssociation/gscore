%define name	gscore
%define version	0.0.8
%define release 7

Name: 	 	%{name}
Summary: 	Musical score editor
Version: 	%{version}
Release: 	%{release}

Source0:		http://www.gscore.org/targz/%{name}-%{version}.tar.bz2
source1:		.abf.yml
Patch0:		gscore-0.0.8-install.patch.bz2
patch1:		gscore-0.0.8.gmodule.patch
URL:		http://www.gscore.org/
License:	GPL
Group:		Publishing
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	scons

%description
Gscore is a non-page-oriented notation program, allowing you to easily write
your scores, as well as import and export in abc format.

%prep
%setup -q
%patch0 -p1 -b .install
%patch1 -p1 -b .gmodule

%build
scons

%install
DESTDIR=%{buildroot} scons install

#menu
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=GScore
Comment=Musical Score Editor
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Office-Publishing;Sound;Player;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO VERSION
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.8-6mdv2011.0
+ Revision: 619258
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.8-5mdv2010.0
+ Revision: 429325
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.0.8-4mdv2009.0
+ Revision: 240798
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 0.0.8-2mdv2008.0
+ Revision: 72663
- fix XDG migration
- convert menu to XDG
- use %%mkrel

  + Pascal Terjan <pterjan@mandriva.org>
    - Import gscore



* Wed Dec 29 2004 Austin Acton <austin@mandrake.org> 0.0.8-1mdk
- 0.0.8
- rediff; scons: suXor, Abel Cheung: r0X0r

* Mon Dec 20 2004 Abel Cheung <deaddog@mandrake.org> 0.0.7-2mdk
- P0: Now it doesn't need files located under /home
- I'll curse scons until it disappears from this world

* Wed Dec 1 2004 Austin Acton <austin@mandrake.org> 0.0.7-1mdk
- initial package
