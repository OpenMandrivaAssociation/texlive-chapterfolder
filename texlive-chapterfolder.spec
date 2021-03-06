# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/chapterfolder
# catalog-date 2008-02-29 20:00:41 +0100
# catalog-license lppl
# catalog-version 2.0.1
Name:		texlive-chapterfolder
Version:	2.0.1
Release:	11
Summary:	Package for working with complicated folder structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chapterfolder
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package simplifies working with folder structures that
match the chapter/section/subsection structure. It provides
macros to define a folder that contains the file for a
chapter/section/subsection, and provides macros that allow
inclusion without using the full path, rather the path relative
to the current folder of the chapter/section/subsection. It
makes easy changing the name of a folder, for example.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chapterfolder/chapterfolder.sty
%doc %{_texmfdistdir}/doc/latex/chapterfolder/chapterfolder.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chapterfolder/chapterfolder.dtx
%doc %{_texmfdistdir}/source/latex/chapterfolder/chapterfolder.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0.1-2
+ Revision: 750102
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0.1-1
+ Revision: 718034
- texlive-chapterfolder
- texlive-chapterfolder
- texlive-chapterfolder
- texlive-chapterfolder
- texlive-chapterfolder

