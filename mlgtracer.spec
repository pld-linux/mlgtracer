%define	_released	200801312023
Summary:	Multi Looking Glass Tracer
Name:		mlgtracer
Version:	0.%{_released}
Release:	1
License:	GPL v3
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/mlgtracer/%{name}-%{_released}.tgz
# Source0-md5:	c6ccbba2cc066edc9e770e9e355c4ec7
URL:		http://sourceforge.net/projects/mlgtracer
Requires:	vilistextum
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mlgtracer is set of scripts which allow use many looking glassess from
one space. It's aimed to help administrators, who want to check how
some ip is accessible from network, and don't like waste time for
visiting many looking-glasses around the world.

%description -l pl.UTF-8
mlgtracer jest zestawem skryptów do używania wielu publicznie
dostępnych looking-glass z jednego miejsca. Jest przeznaczony by
pomóc administratorom, chcącym sprawdzić jak jakieś adresy ip są
dostępne z sieci i nie chcących marnować czasy by sprawdzać to po
koleji z różnych looking-glass.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/lib,%{_bindir}}

%{__make} links \
	DEST=$RPM_BUILD_ROOT%{_bindir} \
	SRC=%{_datadir}/%{name}

cp -r lib/lib.* $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.PL
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/lib/lib.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
