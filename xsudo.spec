Summary:	xsudo permit execute X-application with sudo
Name:		xsudo
Version:	0.4.0
Release:	9
License:	GPLv3+
Group:		System/Base
Url:		http://www.mageialinux.ru
Source0:	%{name}
Source1:	add2sudoers
Source2:	rmfromsudoers
Source3:	sudoers4user
Source4:	add2sudoers.desktop
Source5:	rmfromsudoers.desktop
Source6:	add2sudoers.png
Source7:	rmfromsudoers.png
BuildArch:	noarch
Requires:	sudo

%description
xsudo permit execute X-application with sudo.

%package -n %{name}-sudoers
Summary:	GUI for adding users to /etc/sudoers and for deleting users from /etc/sudoers
Group:		System/Base
Requires:	%{name} = %{version}
Requires:	zenity
Requires:	beesu

%description -n %{name}-sudoers
GUI for adding users to /etc/sudoers and for deleting users from /etc/sudoers.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/applications/
install -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/pixmaps/
install -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/pixmaps/

%post
A=`cat /etc/sudoers | grep "DISPLAY XAUTHORITY XAUTHLOCALHOSTNAME"`
B=`cat /etc/sudoers | grep "# Defaults requiretty"`
if [ -z "$A" ]
then
  echo "Defaults env_keep += \"DISPLAY XAUTHORITY XAUTHLOCALHOSTNAME\"" >> /etc/sudoers
fi
if [ -z "$B" ]
then
  sed -i '/requiretty/s/^Defaults/# Defaults/g' /etc/sudoers
fi

%files
%{_bindir}/%{name}

%files -n %{name}-sudoers
%{_bindir}/add2sudoers
%{_bindir}/rmfromsudoers
%{_bindir}/sudoers4user
%{_datadir}/applications/add2sudoers.desktop
%{_datadir}/applications/rmfromsudoers.desktop
%{_datadir}/pixmaps/add2sudoers.png
%{_datadir}/pixmaps/rmfromsudoers.png

