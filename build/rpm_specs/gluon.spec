%define release 1
%define _sharedstatedir /var/lib
%define build_timestamp %(date +"%Y%m%d")

Summary:          OpenStack Gluon Framework
Name:             gluon
Version:          0.0.1
Release:          %{release}_%{build_timestamp}

License:          Apache 2.0
Group:            Applications/Internet
Source0:          gluon.tar.gz
Url:              https://github.com/openstack/gluon
BuildArch:        noarch

# disabled until systemd is available on build servers
#BuildRequires:    systemd

Vendor:           OpenStack <openstack-dev@lists.openstack.org>
Packager:         Georg Kunz <georg.kunz@ericsson.com>

Requires:         python-pbr
Requires:         python-click
Requires:         python-six
Requires:         python-requests
Requires:         python-yaml
Requires:         python-sqlalchemy
Requires:         python2-babel
Requires:         python2-oslo-db
Requires:         python2-oslo-config
Requires:         python2-oslo-versionedobjects
Requires:         python2-oslo-log
Requires:         python2-oslo-utils
Requires:         python2-oslo-i18n
Requires:         python2-wsme
Requires:         pytz

# disabled until systemd is available on build servers
#Requires(post):   systemd
#Requires(preun):  systemd
#Requires(postun): systemd

%description
OpenStack Gluon framework for NFV networking

%prep
%setup -q
cat << EOF > %{_builddir}/openstack-proton-server.service
[Unit]
Description=OpenStack Proton Server
After=syslog.target network.target

[Service]
Type=simple
TimeoutStartSec=0
Restart=always
User=proton
ExecStart=/usr/bin/proton-server --config-file /etc/proton/proton.conf --logfile /var/log/proton/api.log

[Install]
WantedBy=multi-user.target
EOF

cat << EOF > %{_builddir}/openstack-proton-shim-server.service
[Unit]
Description=OpenStack Proton Shim Server
After=syslog.target network.target

[Service]
Type=simple
TimeoutStartSec=0
Restart=always
User=proton
ExecStart=/usr/bin/proton-shim-server --config-file /etc/proton/proton-shim.conf --logfile /var/log/proton/shim.log

[Install]
WantedBy=multi-user.target
EOF

%install
python setup.py install -O1 --root=%{buildroot} --record=INSTALLED_FILES --prefix=/usr
mkdir -p %{buildroot}/usr/lib/systemd/system
install %{_builddir}/openstack-proton-server.service %{buildroot}/usr/lib/systemd/system
install %{_builddir}/openstack-proton-shim-server.service %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}%{_sharedstatedir}/proton
mkdir -p %{buildroot}%{_localstatedir}/log/proton
mkdir -p %{buildroot}%{_localstatedir}/run/proton
mkdir -p %{buildroot}%{_sysconfdir}/proton
install %{_builddir}/%{name}-%{version}/etc/proton/proton.conf.sample %{buildroot}%{_sysconfdir}/proton/proton.conf
install %{_builddir}/%{name}-%{version}/etc/shim/proton-shim.conf.sample %{buildroot}%{_sysconfdir}/proton/proton-shim.conf


%pre
getent group proton >/dev/null || groupadd -r proton --gid 201
if ! getent passwd proton >/dev/null; then
  useradd -u 201 -r -g proton -G proton,nobody -d %{_sharedstatedir}/proton -s /sbin/nologin -c "OpenStack Proton Server" proton
fi
exit 0


%post
# systemd scriplets disabled until systemd is available on build servers
#%systemd_post openstack-proton-server
if [ $1 -eq 1 ] ; then
        # Initial installation
        systemctl preset openstack-proton-server >/dev/null 2>&1 || :
fi
systemctl start openstack-proton-server

# systemd scriplets disabled until systemd is available on build servers
#%systemd_post openstack-proton-shim-server
if [ $1 -eq 1 ] ; then
        # Initial installation
        systemctl preset openstack-proton-shim-server >/dev/null 2>&1 || :
fi
systemctl start openstack-proton-shim-server


%preun
# systemd scriplets disabled until systemd is available on build servers
#%systemd_preun openstack-proton-server
if [ $1 -eq 0 ] ; then
        # Package removal, not upgrade
        systemctl --no-reload disable openstack-proton-server > /dev/null 2>&1 || :
        systemctl stop openstack-proton-server > /dev/null 2>&1 || :
fi

#%systemd_preun openstack-proton-shim-server
if [ $1 -eq 0 ] ; then
        # Package removal, not upgrade
        systemctl --no-reload disable openstack-proton-shim-server > /dev/null 2>&1 || :
        systemctl stop openstack-proton-shim-server > /dev/null 2>&1 || :
fi


%postun
# systemd scriplets disabled until systemd is available on build servers
#%systemd_postun_with_restart openstack-proton-server
#%systemd_postun_with_restart openstack-proton-shim-server
systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
        # Package upgrade, not uninstall
        systemctl try-restart openstack-proton-server >/dev/null 2>&1 || :
fi

systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
        # Package upgrade, not uninstall
        systemctl try-restart openstack-proton-shim-server >/dev/null 2>&1 || :
fi


%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%attr(644,root,root) /usr/lib/systemd/system/openstack-proton-server.service
%attr(644,root,root) /usr/lib/systemd/system/openstack-proton-shim-server.service
%dir %attr(700,proton,root) %{_sysconfdir}/proton
%attr(640,proton,root) %{_sysconfdir}/proton/proton.conf
%attr(640,proton,root) %{_sysconfdir}/proton/proton-shim.conf
%dir %attr(750,proton,root) %{_localstatedir}/log/proton
%dir %attr(750,proton,root) %{_localstatedir}/run/proton
%dir %attr(755,proton,root) %{_sharedstatedir}/proton
