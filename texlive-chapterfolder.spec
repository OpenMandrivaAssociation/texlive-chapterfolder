%global tl_name chapterfolder
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.1
Release:	%{tl_revision}.1
Summary:	Package for working with complicated folder structures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chapterfolder
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chapterfolder.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package simplifies working with folder structures that match the
chapter/section/subsection structure. It provides macros to define a
folder that contains the file for a chapter/section/subsection, and
provides macros that allow inclusion without using the full path, rather
the path relative to the current folder of the
chapter/section/subsection. It makes easy changing the name of a folder,
for example.

