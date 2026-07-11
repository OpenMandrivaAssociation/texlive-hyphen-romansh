%global tl_name hyphen-romansh
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Romansh hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-romansh
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-romansh.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Romansh. All Romansh idioms and Rumantsch
Grischun taken into account, developed in collaboration with Fundaziun
Medias Rumantschas (Romansh news agency) and Lia Rumantscha (Romansh
umbrella organisation).

