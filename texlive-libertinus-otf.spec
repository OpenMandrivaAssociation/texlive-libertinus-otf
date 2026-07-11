%global tl_name libertinus-otf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.34
Release:	%{tl_revision}.1
Summary:	Support for Libertinus OpenType
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertinus-otf
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers LuaLaTeX/XeLaTeX support for the Libertinus OpenType
fonts maintained by Khaled Hosny. Missing fonts are defined via several
font feature settings. The Libertinus fonts are similar to Libertine and
Biolinum, but come with math symbols.

