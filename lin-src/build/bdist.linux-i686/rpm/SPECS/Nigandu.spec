%define name Nigandu
%define version 1.0.0
%define unmangled_version 1.0.0
%define release 1

Summary: Nigandu is the first cross-platform  dictionary application for English to Tamil word meanings.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Noortheen Raja J <jnoortheen@gmail.com>

%description
Nigandu is a dictionary application for English to Tamil word meanings.

%prep
%setup -n %{name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build

%install
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%define __prelink_undo_cmd %{nil}
