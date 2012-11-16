Name:       cloudstart
Version:    0.0.1 
Release:    1%{?dist}
Summary:    cloudstart initialization scripts
Group:      System Environment/Daemons
License:    MIT 
URL:        https://github.com/jasonhancock/cloudstart
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-buildroot
BuildArch:  noarch

%description

Scripts to bootstrap cloud instances. Trying to be simpler than cloud-init

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p ${RPM_BUILD_ROOT}%{_initrddir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/cloudstart/plugins

install -m 0755 cloudstart ${RPM_BUILD_ROOT}%{_initrddir}/cloudstart
install -m 0644 sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/cloudstart

for f in `ls plugins/`
do
    install -m 0755 plugins/$f ${RPM_BUILD_ROOT}/usr/share/cloudstart/plugins/
done

%post
/sbin/chkconfig --add cloudstart

%preun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del cloudstart
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_initrddir}/cloudstart
%{_sysconfdir}/sysconfig/cloudstart
/usr/share/cloudstart/plugins/*

%changelog
