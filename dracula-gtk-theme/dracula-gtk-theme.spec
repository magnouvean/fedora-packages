Name:           dracula-gtk-theme
Version:        4.0.0
Release:        0
Summary:        Dark theme for GTK

License:        GPL-3.0-only
URL:            https://github.com/dracula/gtk
Source0:        %url/releases/download/v%{version}/Dracula.tar.xz

BuildArch:      noarch


%description
The kde parts of dracula GTK port


%prep

%setup -c -q

%build

%install
mkdir -p %{buildroot}/usr/share/themes/
cp -a Dracula %{buildroot}/usr/share/themes/
cp -a Dracula-alt-style %{buildroot}/usr/share/themes/
cp -a Dracula-slim %{buildroot}/usr/share/themes/
cp -a Dracula-slim-standard-buttons %{buildroot}/usr/share/themes/
cp -a Dracula-standard-buttons %{buildroot}/usr/share/themes/

%files
%{_datadir}/themes/


%changelog
* Fri Jun 09 2023 execowl <account.fedoraproject.org/user/execowl>
- Initial release
