Name:		texlive-libertinus-otf
Version:	68333
Release:	1
Summary:	Support for Libertinus OpenType
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libertinus-otf
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers LuaLaTeX/XeLaTeX support for the Libertinus
OpenType fonts maintained by Khaled Hosny. Missing fonts are
defined via several font feature settings. The Libertinus fonts
are similiar to Libertine and Biolinum, but come with math
symbols.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/libertinus-otf
%doc %{_texmfdistdir}/doc/fonts/libertinus-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
