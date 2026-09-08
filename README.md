# crossprobe

# Anonymous
This repository contains all the research output about vulnerabilities in Prolink Smart Plug.

# Prolink 13A Smart Plug Model Version: DS-3202M-UKv3

## Affected Product

 Prolink 13A Smart Plug Model Version: DS-3202M-UKv3

## Affected Vendor

 Prolink

## CVE Number

[CVE-2025-66974] ([https://www.cve.org/CVERecord?id=CVE-2025-66974)])

## Summary

The lack of a verification mechanism at the Prolink Smart Plug device to bind a application of legitimate user using its authentication token to the smart plug being provisioned. If the legitimate authentication token is replaced with the attacker's authentication token and the Prolink 13A Smart Plug accepts these replayed packets, then this vulnerability exits. Because of this vulnerability, the legitimate IoT device gets provisioned on the attacker   s mobile application i.e., the attacker   s cloud account of the controller.

## Tested Versions

Prolink Smart Plug - (Model: DS-3202M and Version application: 2.7.2)

## Product URLs

[Website] (https://prolink2u.com/collections/data?filter.p.m.custom.filter_category=Smart+Home)

## CVSSv3 Score

TBA

## CWE

TBA

## Details

To exploit the vulnerability, an attacker replays the Wi-Fi packets captured during the legitimate provisioning of the device within the attacker's token validity
