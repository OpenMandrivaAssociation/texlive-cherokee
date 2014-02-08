# revision 21046
# category Package
# catalog-ctan /fonts/cherokee
# catalog-date 2008-12-25 20:17:19 +0100
# catalog-license noinfo
# catalog-version undef
Name:		texlive-cherokee
Version:	20081225
Release:	3
Summary:	A font for the Cherokee script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cherokee
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cherokee.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cherokee.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081225-2
+ Revision: 750150
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081225-1
+ Revision: 718047
- texlive-cherokee
- texlive-cherokee
- texlive-cherokee
- texlive-cherokee
- texlive-cherokee

