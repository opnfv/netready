%define release 1
%define _sharedstatedir /var/lib

Summary:   OpenStack Gluon Framework
Name:      gluon
Version:   0.0.1
Release:   %{release}%{?git}%{?dist}

License:   Apache 2.0
Group:     Applications/Internet
Source0:   gluon.tar.gz
Url:       https://github.com/openstack/gluon
BuildArch: noarch

Vendor:    OpenStack <openstack-dev@lists.openstack.org>
Packager:  Georg Kunz <georg.kunz@ericsson.com>

Requires:  python-pbr
Requires:  python-click
Requires:  python-six
Requires:  python-requests
Requires:  python-yaml
Requires:  python-sqlalchemy
Requires:  python2-babel
Requires:  python2-oslo-db
Requires:  python2-oslo-config
Requires:  python2-oslo-versionedobjects
Requires:  python2-oslo-log
Requires:  python2-oslo-utils
Requires:  python2-oslo-i18n
Requires:  python2-wsme
Requires:  pytz

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

cat << EOF > %{_builddir}/proton.conf
[DEFAULT]
state_path = /var/lib/proton
EOF


%install
python setup.py install -O1 --root=%{buildroot} --record=INSTALLED_FILES --prefix=/usr
mkdir -p %{buildroot}/usr/lib/systemd/system
install %{_builddir}/openstack-proton-server.service %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}%{_sharedstatedir}/proton
mkdir -p %{buildroot}%{_localstatedir}/log/proton
mkdir -p %{buildroot}%{_localstatedir}/run/proton
mkdir -p %{buildroot}%{_sysconfdir}/proton
install %{_builddir}/proton.conf %{buildroot}%{_sysconfdir}/proton


%pre
getent group proton >/dev/null || groupadd -r proton --gid 201
if ! getent passwd proton >/dev/null; then
  useradd -u 201 -r -g proton -G proton,nobody -d %{_sharedstatedir}/proton -s /sbin/nologin -c "OpenStack Proton Server" proton
fi
exit 0


%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%attr(644,root,root) /usr/lib/systemd/system/openstack-proton-server.service
%attr(640,proton,root) /etc/proton/proton.conf
%attr(750,proton,root) /var/log/proton
%attr(750,proton,root) /var/run/proton
%attr(755,proton,root) /var/lib/proton
