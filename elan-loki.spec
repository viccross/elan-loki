Name:       elan-loki
%{!?_version: %define _version 0.0 }
Version:    %{_version}
Release:    1%{?dist}
Summary:    Loki and Promtail for the ELAN
License:    AGPL-3.0-only
BuildArch:  s390x
BuildRequires: go
BuildRequires: make
%define debug_package %{nil}
%description
This package contains Grafana Loki and Promtail built for the ELAN as
part of z/VM ESI. It provides a configuration of Promtail that works
with Mosquitto.

%prep
%setup -q

%build
make loki
make promtail

%install
mkdir -p usr/local/bin
mkdir -p etc/loki
cp loki/loki usr/local/bin/
cp clients/promtail/promtail usr/local/bin/
cp etc/loki/mqtt-promtail.yaml etc/loki/
cp etc/loki/loki.yaml etc/loki/

%files
/etc/loki/mqtt-promtail.yaml
/etc/loki/loki.yaml
/usr/local/bin/loki
/usr/local/bin/promtail
/usr/local/systemd/system/mqtt-promtail.service
/usr/local/systemd/system/loki.service

%post
systemctl enable loki.service
systemctl enable mqtt-promtail.service

%changelog
Fri Mar  1 2024 Vic Cross <viccross@au.ibm.com> - 0.0.1-1
- Initial
