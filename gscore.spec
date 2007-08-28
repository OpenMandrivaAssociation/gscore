%define name	gscore
%define version	0.0.8
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Musical score editor
Version: 	%{version}
Release: 	%{release}

Source:		http://www.gscore.org/targz/%{name}-%{version}.tar.bz2
Patch0:		gscore-0.0.8-install.patch.bz2
URL:		http://www.gscore.org/
License:	GPL
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	libglade2.0-devel
BuildRequires:	gtk2-devel
BuildRequires:	scons

%description
Gscore is a non-page-oriented notation program, allowing you to easily write
your scores, as well as import and export in abc format.

%prep
%setup -q
%patch0 -p1 -b .install

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
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
Categories=X-MandrivaLinux-Office-Publishing;Sound;Player
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO VERSION
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
