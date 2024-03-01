Name:       elan-loki
%{!?_version: %define _version 0.0 }
Version:    %{_version}
Release:    1%{?dist}
Summary:    Loki and Promtail for the ELAN
License:    AGPL-3.0-only
BuildArch:  s390x
BuildRequires: golang
BuildRequires: make
BuildRequires: systemd-devel
%define debug_package %{nil}
%description
This package contains Grafana Loki and Promtail built for the ELAN as
part of z/VM ESI. It provides a configuration of Promtail that works
with Mosquitto.

%build
make all

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/systemd/system
mkdir -p %{buildroot}/etc/loki
install -m 755 cmd/loki/loki %{buildroot}/usr/local/bin/loki
install -m 755 cmd/loki-canary/loki-canary %{buildroot}/usr/local/bin/loki-canary
install -m 755 clients/cmd/promtail/promtail %{buildroot}/usr/local/bin/promtail
install -m 755 cmd/logcli/logcli %{buildroot}/usr/local/bin/logcli
install -m 755 systemd/promtail-mqtt %{buildroot}/usr/local/bin/promtail-mqtt
install -m 644 etc/promtail-mqtt.yaml %{buildroot}/etc/loki/promtail-mqtt.yaml
install -m 644 etc/loki.yaml %{buildroot}/etc/loki/loki.yaml
install -m 644 systemd/loki.service %{buildroot}/usr/local/systemd/system/loki.service
install -m 644 systemd/promtail-mqtt.service %{buildroot}/usr/local/systemd/system/promtail-mqtt.service

%files
/etc/loki/promtail-mqtt.yaml
/etc/loki/loki.yaml
/usr/local/bin/logcli
/usr/local/bin/loki
/usr/local/bin/loki-canary
/usr/local/bin/promtail
/usr/local/bin/promtail-mqtt
/usr/local/systemd/system/promtail-mqtt.service
/usr/local/systemd/system/loki.service

%post
systemctl enable loki.service
systemctl enable mqtt-promtail.service

%changelog
* Fri Mar  1 2024 Vic Cross <viccross@au.ibm.com> - 0.0.1-1
  - Initial
