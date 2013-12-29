Summary:	Simple bridge between colord and X
Name:		xiccd
Version:	0.2.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://github.com/agalakhov/xiccd/archive/v%{version}.tar.gz
# Source0-md5:	58da0df3694815594ebca8a41fc21d6f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	colord-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXrandr-devel
Requires:	colord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xiccd is a simple bridge between colord and X.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xiccd

