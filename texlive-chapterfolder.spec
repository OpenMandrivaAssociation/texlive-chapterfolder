Name:		texlive-chapterfolder
Version:	2.0.1
Release:	1
Summary:	Package for working with complicated folder structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chapterfolder
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package simplifies working with folder structures that
match the chapter/section/subsection structure. It provides
macros to define a folder that contains the file for a
chapter/section/subsection, and provides macros that allow
inclusion without using the full path, rather the path relative
to the current folder of the chapter/section/subsection. It
makes easy changing the name of a folder, for example.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
