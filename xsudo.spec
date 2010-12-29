Summary:        xsudo permit execute X-application with sudo
Name:           xsudo
Version:        0.1.0
Release:        %mkrel 1
License:        GPLv2+
Group:          System/Base
Source0:        %{name}
BuildArch:      noarch
Requires:	sudo

%description
xsudo permit execute X-application with sudo

%prep

%build

%install
rm -rf %{buildroot}

mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
cp %SOURCE0  ${RPM_BUILD_ROOT}/%{_bindir}/xsudo

%clean
rm -rf %{buildroot}

%post

cat /etc/sudoers | grep "DISPLAY XAUTHORITY XAUTHLOCALHOSTNAME" && exit 0
echo "Defaults env_keep += \"DISPLAY XAUTHORITY XAUTHLOCALHOSTNAME\"" >> /etc/sudoers
sed -i '/requiretty/s/^Defaults/# Defaults/g' /etc/sudoers

%files
%defattr(-, root, root, -)

%{_bindir}/xsudo