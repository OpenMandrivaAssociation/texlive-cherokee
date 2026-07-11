%global tl_name cherokee
%global tl_revision 21046

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A font for the Cherokee script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cherokee
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cherokee.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cherokee.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Cherokee script was designed in 1821 by Segwoya. The alphabet is
essentially syllabic, only 6 characters (a e i o s u) correspond to
Roman letters: the font encodes these to the corresponding roman letter.
The remaining 79 characters have been arbitrarily encoded in the range
38-122; the cherokee package provides commands that map each such
syllable to the appropriate character; for example, Segwoya himself
would be represented \Cse\Cgwo\Cya. The font is distributed as Metafont
source; it works very poorly in modern environments, and could do with
expert attention (if you are interested, please contact the CTAN team
for details).

