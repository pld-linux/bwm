Summary:	Bandwidth monitor - display bandwidth usage on all interfaces
Summary(pl.UTF-8):   Bandwidth monitor - wyświetlanie obciążenia na interfejsach
Name:		bwm
Version:	1.1.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://ftp.debian.org/debian/pool/main/b/bwm/%{name}_%{version}.orig.tar.gz
# Source0-md5:	51021a036acb92d2bda0c0c0483f9552
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bandwidth monitor is a very simple utility that allows the user to
view the bandwidth currently being consumed to and from each network
interface, the total bandwidth in use on each interface, and the total
bandwidth in use on all interfaces.

%description -l pl.UTF-8
Bandwidth monitor jest bardzo małym i prostym narzędziem pozwalającym
użytkownikowi obserwować bieżące użycie łącza. Pokazuje ruch na każdym
interfejsie z osobna oraz podsumowanie wszystkich interfejsów.

%prep
%setup -q -n %{name}-%{version}.orig

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bwm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt readme.txt
%attr(755,root,root) %{_bindir}/*
