Summary: 	An uncommonly powerful .NET configuration library
Name:		nini
Version:	1.1.0
Release:	1
Group: 		Development/Other
License:	X11/MIT
URL: 		http://nini.sourceforge.net/
Source0: 	Nini-%{version}.zip
BuildArch:	noarch

BuildRequires:	mcs
BuildRequires:	nant
BuildRequires:	unzip
BuildRequires: 	mono-devel
    
%description
Nini is an uncommonly powerful .NET configuration library designed to help 
build highly configurable applications quickly.
       
%prep
%setup -qn Nini
       
%build
cd Source
mcs -target:library -out:Nini.dll -reference:System.dll -reference:System.Xml.dll -define:MONO_1_1 -define:NOSTRONG AssemblyInfo.cs Ini/*.cs Config/*.cs Util/*.cs
cat << EOF > nini-1.1.pc
prefix=%{_prefix}
assemblies_dir=\${prefix}/lib/nini
Libraries=\${assemblies_dir}/Nini.dll

Name: Nini
Description: An uncommonly powerful .NET configuration library
Version: %{version}
Libs: -r:Nini.dll
EOF

%install
cd Source
mkdir -p %{buildroot}%{_prefix}/lib/nini
cp Nini.dll %{buildroot}%{_prefix}/lib/nini/
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cp nini-1.1.pc %{buildroot}%{_datadir}/pkgconfig/

%files
%{_prefix}/lib/nini
%{_datadir}/pkgconfig/nini-1.1.pc



%changelog
* Thu May 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-1
+ Revision: 800460
- imported package nini

