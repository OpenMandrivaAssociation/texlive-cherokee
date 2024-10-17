Name:		texlive-cherokee
Version:	21046
Release:	2
Summary:	A font for the Cherokee script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cherokee
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cherokee.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cherokee.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Cherokee script was designed in 1821 by Segwoya. The
alphabet is essentially syllabic, only 6 characters (a e i o s
u) correspond to Roman letters: the font encodes these to the
corresponding roman letter. The remaining 79 characters have
been arbitrarily encoded in the range 38-122; the cherokee
package provides commands that map each such syllable to the
appropriate character; for example, Segwoya himself would be
represented \Cse\Cgwo\Cya.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cherokee/cherokee.mf
%{_texmfdistdir}/fonts/tfm/public/cherokee/cherokee.tfm
%{_texmfdistdir}/tex/latex/cherokee/cherokee.sty
%doc %{_texmfdistdir}/doc/fonts/cherokee/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
