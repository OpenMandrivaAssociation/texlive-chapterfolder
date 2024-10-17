Name:		texlive-chapterfolder
Version:	15878
Release:	2
Summary:	Package for working with complicated folder structures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chapterfolder
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
