Version: 3.0.2
Release: 0
URL:     https://github.com/ryanoasis/nerd-fonts

%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        fira-code-nerd
%global fontsummary       fira code with nerd fonts symbols
%global fonts             *.ttf
%global fontdescription   %{expand:
Fira Code font with nerd font icons included
}

Source0:  %url/releases/download/v%{version}/FiraCode.tar.xz

%fontpkg

%prep
%setup -c %{name}-%{version}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Aug 25 2023 execowl <account.fedoraproject.org/user/execowl>
- Initial RPM release
