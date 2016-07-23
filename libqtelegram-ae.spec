%global origname libqtelegram-aseman-edition
%global channel stable

Name:           libqtelegram-ae
Version:        10.0.0
Release:        1%{?dist}
Summary:        Fork of libqtelegram by Aseman Team

License:        GPLv3+
URL:            https://github.com/Aseman-Land/libqtelegram-aseman-edition
Source0:        %{url}/archive/v%{version}-%{channel}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  openssl-devel
# Only compile-time
BuildRequires:  qt5-qtmultimedia-devel

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
Requires:       openssl-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -n %{origname}-%{version}-%{channel}
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %qmake_qt5 .. \
      CONFIG+=typeobjects \
      QMAKE_CFLAGS_ISYSTEM= \
      PREFIX=%{_prefix} \
      INSTALL_LIBS_PREFIX=%{_libdir} \
      INSTALL_HEADERS_PREFIX=%{_includedir}
popd
%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so

%changelog
* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 10.0.0-1
- Initial package
