"""
Default ConfigUI for S2-D8D16 data recorders 
"""

from base64 import b64decode

DEFAULT_CONFIG_UI = b64decode(
    b'd3dV3kAoRjBQBYdHZW5lcmFsQAXzUAWLRGV2aWNlIE5hbWVQAYMI/39RJIFAUBXYQSBjdX'
    b'N0b20gbmFtZSBmb3IgdGhlIHJlY29yZGVyLiBOb3QgdGhlIHNhbWUgYXMgdGhlIHZvbHVt'
    b'ZSBsYWJlbC4gNjQgY2hhcmFjdGVycyBtYXhpbXVtLkAF81AFjERldmljZSBOb3Rlc1ABgw'
    b'n/f1EkggEAUBXSQ3VzdG9tIG5vdGVzIGFib3V0IHRoZSByZWNvcmRlciAocG9zaXRpb24s'
    b'IHVzZXIgSUQsIGV0Yy4pLiAyNTYgY2hhcmFjdGVycyBtYXhpbXVtLlE0gQNABUCZUAWVQ3'
    b'VzdG9tIFJlY29yZGluZyBUYWdzUAGDF/9/UQSAUSSBQFAV8UtleXdvcmRzIGZvciBvcmdh'
    b'bml6aW5nIGFuZCBpZGVudGlmeWluZyByZWNvcmRpbmdzLCBzZXBhcmF0ZWQgYnkgY29tbW'
    b'Egb3Igc3BhY2UuIExpbWl0IGlzIDIwIHRhZ3MsIDY0IGNoYXJhY3RlcnMuQAX7UAWTUmVj'
    b'b3JkaW5nIERpcmVjdG9yeVABgxT/f1EEhlJFQ09SRFEkgRBQFJNDb25maWdbMHgxNkZGN0'
    b'ZdPT0wUBW5RGlyZWN0b3J5IGZvciBzZXJpYWxpemVkIHJlY29yZGluZ3MuIDE2IGNoYXJh'
    b'Y3RlciBtYXhpbXVtQAVAo1AFlVJlY29yZGluZyBGaWxlIFByZWZpeFABgxX/f1EkgRBQFe'
    b'hQcmVmaXggZm9yIHNlcmlhbGl6ZWQgcmVjb3JkaW5nIG5hbWVzLiBJZiBibGFuaywgZGV2'
    b'aWNlIHNlcmlhbCBudW1iZXIgd2lsbCBiZSB1c2VkLiAxNiBjaGFyYWN0ZXIgbWF4aW11bV'
    b'AUk0NvbmZpZ1sweDE2RkY3Rl09PTBAB0E8UAWPRmlsZSBOYW1lIFN0eWxlUAGDFv9/UQGB'
    b'AVAVQPxUaW1lLUJhc2VkIGZpbGUgbmFtZXMgdXNlIGEgZGlyZWN0b3J5IGJhc2VkIG9uIH'
    b'RoZSBkYXRlLCBhbmQgZmlsZSBuYW1lIGJhc2VkIG9uIHRoZSBzZWNvbmRzIHNpbmNlIG1p'
    b'ZG5pZ2h0LgpTZXJpYWxpemVkIGZpbGUgbmFtZXMgdXNlIHRoZSBzcGVjaWZpZWQgZGlyZW'
    b'N0b3J5IGFuZCBmaWxlIG5hbWUgcHJlZml4LCBmb2xsb3dlZCBieSBhIG51bWJlci4gCk51'
    b'bWJlciBpcyByZXNldCB3aGVuIGRpcmVjdG9yeSBvciBwcmVmaXggY2hhbmdlcy5BB41QBY'
    b'pUaW1lIEJhc2VkQQeNUAWKU2VyaWFsaXplZEAHQKlQBYtCdXR0b24gTW9kZVABgxD/f1EB'
    b'gQBQFb9PbmUgU2Vjb25kIFByZXNzIHdpbGwgZGlzYWJsZSAzLXNlY29uZCBwcmVzcyBmb3'
    b'IgYmF0dGVyeSBjaGVjay5BB5dQBZRJbW1lZGlhdGUgU3RhcnQvU3RvcEEHolAFn09uZSBT'
    b'ZWNvbmQgUHJlc3MgZm9yIFN0YXJ0L1N0b3BBB41QBYpTdGFydC1Pbmx5QBdBFFAFjlBsdW'
    b'ctSW4gQWN0aW9uUAGDCv9/UQGBAVAVrVNldCBhY3Rpb24gZm9yIGRldmljZSB3aGVuIHBs'
    b'dWdnZWQgaW4gdG8gVVNCLkEHtVAFskltbWVkaWF0ZWx5IHN0b3AgcmVjb3JkaW5nIGFuZC'
    b'BhcHBlYXIgYXMgVVNCIGRyaXZlQQezUAWwQ29tcGxldGUgcmVjb3JkaW5nIGJlZm9yZSBh'
    b'cHBlYXJpbmcgYXMgVVNCIGRyaXZlQQewUAWtSWdub3JlOiBzdG9wIHJlY29yZGluZyB3aG'
    b'VuIGJ1dHRvbiBpcyBwcmVzc2VkQQelUAWiU3RhcnQgcmVjb3JkaW5nIHdoZW4gVVNCIGNv'
    b'bm5lY3RlZEAj51ABgwv/f1AV3kVudGVyIGxvY2FsIHRpbWV6b25lJ3Mgb2Zmc2V0IGZyb2'
    b'0gVVRDIHRpbWUuIEltcGFjdHMgdGltZXN0YW1wIGluZm9ybWF0aW9uIG9uIHJlY29yZGlu'
    b'ZyBmaWxlcy5AL4BAD4BAT4BAKEkZUAWIVHJpZ2dlcnNAB0DaUAWMVHJpZ2dlciBNb2RlUA'
    b'GDEv9/UQGBAFAVQI9EZWxheSBUaGVuIFRyaWdnZXI6IFdhaXQgc3BlY2lmaWVkIHRpbWUs'
    b'IHRoZW4gd2FpdCBmb3IgdHJpZ2dlcgpEZWxheSBPciBUcmlnZ2VyOiBBY3F1aXJlIGFmdG'
    b'VyIHdhaXQgb3Igb24gdHJpZ2dlci4gQmF0dGVyeSBsaWZlIG1heSBiZSByZWR1Y2VkLkEH'
    b'lVAFkkRlbGF5IFRoZW4gVHJpZ2dlckEHk1AFkERlbGF5IE9yIFRyaWdnZXJAMvRQBY1TdG'
    b'FydCBhdCBUaW1lUAGDD/9/UBXbV2FpdCB1bnRpbCBzZXQgdGltZSBiZWZvcmUgZXZhbHVh'
    b'dGluZyBvdGhlciB0cmlnZ2VyIGNvbmRpdGlvbnMsIGluY2x1ZGluZyBhIHJlY29yZGluZy'
    b'BkZWxheUARrlAFlFJlY29yZGluZyBUaW1lIExpbWl0UAGDDf9/USGE////8FAlh1NlY29u'
    b'ZHNAEUCQUAWYUmVjb3JkaW5nIERlbGF5L0ludGVydmFsUAGDDP9/UQGBAFAlh1NlY29uZH'
    b'NRIYMBUYBQFdhUaW1lIGJlZm9yZSBzdGFydGluZyBhIHJlY29yZGluZywgYW5kIHRpbWUg'
    b'YmV0d2VlbiByZWNvcmRpbmdzIGlmICdSZXRyaWdnZXInIGlzIGNoZWNrZWQuQBGvUAWZUm'
    b'Vjb3JkaW5nIEZpbGUgU2l6ZSBMaW1pdFABgxH/f1EhhP////BQJYNLaUJAEECXUAWJUmV0'
    b'cmlnZ2VyUAGDDv9/UBSwQ29uZmlnWzB4REZGN0ZdPT1udWxsIGFuZCBDb25maWdbMHgxMU'
    b'ZGN0ZdPT1udWxsUBXPV2hlbiBzZXQsIFNsYW0gU3RpY2sgd2lsbCByZS1hcm0gYWZ0ZXIg'
    b'cmVjb3JkaW5nIHRpbWUgb3Igc2l6ZSBsaW1pdCBpcyByZWFjaGVkLkAQQKhQBZ5XYWl0IG'
    b'ZvciBBbGwgU2Vuc29yIENvbmRpdGlvbnNQAYMT/39QFf5XaGVuIHNldCwgcmVjb3JkaW5n'
    b'IHdpbGwgb25seSBzdGFydCB3aGVuIGFsbCB0cmlnZ2VycyBhcmUgbWV0LCBvdGhlcndpc2'
    b'UgcmVjb3JkaW5nIHdpbGwgc3RhcnQgd2hlbiBhbnkgc2Vuc29yIGNvbmRpdGlvbiBpcyBt'
    b'ZXRAGEEKUAWQUHJlc3N1cmUgVHJpZ2dlclABgwUAJFEAgQBQFJlDb25maWdbMHgwMUZGMj'
    b'RdICYgMSA9PSAwQILlUAWVUHJlc3N1cmUgVHJpZ2dlciwgTG93UAGDAwAkUQGDAV+QUCWC'
    b'UGFRIYMB1MBQFbNTZXQgdG8gc3RhcnQgc2FtcGxpbmcgd2hlbiBvdXRzaWRlIHByZXNzdX'
    b'JlIHdpbmRvdy5AguZQBZZQcmVzc3VyZSBUcmlnZ2VyLCBIaWdoUAGDBAAkUQGDAa2wUCWC'
    b'UGFRIYMB1MBQFbNTZXQgdG8gc3RhcnQgc2FtcGxpbmcgd2hlbiBvdXRzaWRlIHByZXNzdX'
    b'JlIHdpbmRvdy5AGEEXUAWTVGVtcGVyYXR1cmUgVHJpZ2dlclABgwUBJFEAgQBQFJlDb25m'
    b'aWdbMHgwMUZGMjRdICYgMiA9PSAwQGPqUAWYVGVtcGVyYXR1cmUgVHJpZ2dlciwgTG93UA'
    b'GDAwEkUQKB9lAlgUNREoHYUSKBUFAVtlNldCB0byBzdGFydCBzYW1wbGluZyB3aGVuIG91'
    b'dHNpZGUgdGVtcGVyYXR1cmUgd2luZG93LkBj61AFmVRlbXBlcmF0dXJlIFRyaWdnZXIsIE'
    b'hpZ2hQAYMEASRRAoEjUCWBQ1ESgdhRIoFQUBW2U2V0IHRvIHN0YXJ0IHNhbXBsaW5nIHdo'
    b'ZW4gb3V0c2lkZSB0ZW1wZXJhdHVyZSB3aW5kb3cuQBhBolAFmkFjY2VsZXJhdGlvbiBUcm'
    b'lnZ2VyICgxNmcpUAGDB/8gUBXUTG93IHBvd2VyIHRyaWdnZXIgdXNpbmcgZGlnaXRhbCBh'
    b'Y2NlbGVyb21ldGVyIHdpdGggREMgcmVzcG9uc2UuIE5vIHByZS10cmlnZ2VyIGRhdGEuUQ'
    b'CBAFARgwX/CFARgwf/UFAkgFAUlENvbmZpZ1sweDFmZjIwXSA9PSAwQENAsVAFlkFjY2Vs'
    b'ZXJhdGlvbiBUaHJlc2hvbGRQAYME/yBRAYFQUgOIP7AQEBAQEBBRI4hAMAAAAAAAAFETgF'
    b'AV8kxvdyBwb3dlciB0cmlnZ2VyLiBUaGUgbWluaW11bSBhY2NlbGVyYXRpb24gKHBvc2l0'
    b'aXZlIG9yIG5lZ2F0aXZlKSB0byB0cmlnZ2VyIGEgcmVjb3JkaW5nLiBNdXN0IGJlIGdyZW'
    b'F0ZXIgdGhhbiAwLkAnxlABgwX/IFEBgQdBB5FQBY5YIEF4aXMgVHJpZ2dlckEHkVAFjlkg'
    b'QXhpcyBUcmlnZ2VyQQeRUAWOWiBBeGlzIFRyaWdnZXJAGEGiUAWZQWNjZWxlcmF0aW9uIF'
    b'RyaWdnZXIgKDhnKVABgwf/UFAV1ExvdyBwb3dlciB0cmlnZ2VyIHVzaW5nIGRpZ2l0YWwg'
    b'YWNjZWxlcm9tZXRlciB3aXRoIERDIHJlc3BvbnNlLiBObyBwcmUtdHJpZ2dlciBkYXRhLl'
    b'EAgQBQEYMF/whQEYMH/yBQJIBQFJRDb25maWdbMHgxZmY1MF0gPT0gMEBDQLJQBZZBY2Nl'
    b'bGVyYXRpb24gVGhyZXNob2xkUAGDBP9QUQGCIABSA4g/IAAQABAAEFEjiEAgAAAAAAAAUR'
    b'OAUBXyTG93IHBvd2VyIHRyaWdnZXIuIFRoZSBtaW5pbXVtIGFjY2VsZXJhdGlvbiAocG9z'
    b'aXRpdmUgb3IgbmVnYXRpdmUpIHRvIHRyaWdnZXIgYSByZWNvcmRpbmcuIE11c3QgYmUgZ3'
    b'JlYXRlciB0aGFuIDAuQCfGUAGDBf9QUQGBB0EHkVAFjlggQXhpcyBUcmlnZ2VyQQeRUAWO'
    b'WSBBeGlzIFRyaWdnZXJBB5FQBY5aIEF4aXMgVHJpZ2dlckAPgEBPgEAoRoBQBYxNZWFzdX'
    b'JlbWVudHNACEC6UAWbMTZnIERDIEFjY2VsZXJhdGlvbiAoQ2ggMzIpQCefUAGDAf8gUQGB'
    b'AUEHklAFj0VuYWJsZSBBbGwgQXhlc0AX91AFi1NhbXBsZSBSYXRlUAGDAv8gUQGCAZBQJY'
    b'JIelAUk25vdCBDb25maWdbMHgxZmYyMF1BB4VRAYIMgEEHhVEBggZAQQeFUQGCAyBBB4VR'
    b'AYIBkEEHhFEBgchBB4RRAYFkQQeEUQGBMkEHhFEBgRlBB4RRAYEMQAhBG1AFmjhnIERDIE'
    b'FjY2VsZXJhdGlvbiAoQ2ggODApQCefUAGDAf9QUQGBAUEHklAFj0VuYWJsZSBBbGwgQXhl'
    b'c0AXQNhQBYtTYW1wbGUgUmF0ZVABgwL/UFEBggH0UCWCSHpQFd5Mb3cgcGFzcyBmaWx0ZX'
    b'IgaXMgc2V0IHRvIDI1JSBvZiBkYXRhIHJhdGUsIHNvIGEgZGF0YSByYXRlIG9mIDIwMDBI'
    b'eiBoYXMgYSBMUCBmaWx0ZXIgYXQgNTAwIEh6UBSTbm90IENvbmZpZ1sweDFmZjUwXUEHhV'
    b'EBgg+gQQeFUQGCB9BBB4VRAYID6EEHhVEBggH0QQeEUQGB+kEHhFEBgX1BB4RRAYE/QQeE'
    b'UQGBIEEHhFEBgRBACEEwUAWoQ29udHJvbCBQYWQgVGVtcGVyYXR1cmUvUHJlc3N1cmUgKE'
    b'NoIDU5KUAnQJtRAYEDUAGDAf87UBWlRW5hYmxlL0Rpc2FibGUgc2Vuc29ycyBvbiBjb250'
    b'cm9sIHBhZEEHnFAFmUVuYWJsZSBQcmVzc3VyZSAoQ2ggNTkuMClBB59QBZxFbmFibGUgVG'
    b'VtcGVyYXR1cmUgKENoIDU5LjEpQQelUAWiRW5hYmxlIFJlbGF0aXZlIEh1bWlkaXR5IChD'
    b'aCA1OS4yKUAR41AFi1NhbXBsZSBSYXRlUAGDAv87UBSUQ29uZmlnWzB4MWZmM0JdID09ID'
    b'BQFaRTZXQgc2FtcGxlIGZyZXF1ZW5jeSBmcm9tIDEgdG8gMTAgSHpRAYEKUCWCSHpREYEB'
    b'USGBCkAIQc1QBZlJbmVydGlhbCBNZWFzdXJlbWVudCBVbml0QAdAllAFkEFjcXVpc2l0aW'
    b'9uIE1vZGVQAYMB/ytQJYEgUQGBEEEHilAFg09mZlEBgQBBB6hQBaFBYnNvbHV0ZSBPcmll'
    b'bnRhdGlvbiAoUXVhdGVybmlvbilRAYEIQQeoUAWhUmVsYXRpdmUgT3JpZW50YXRpb24gKF'
    b'F1YXRlcm5pb24pUQGBEEEHj1AFiFJvdGF0aW9uUQGBAkABQIZQBZVPcmllbnRhdGlvbiBE'
    b'YXRhIFJhdGVQAYMCCCtRAYFkUCWCSHpREYEBUSGByFAVvVNhbXBsZSByYXRlIGZvciBkaX'
    b'JlY3Rpb25hbCBkYXRhIGZyb20gMSB0byAyMDAgSHouIENoYW5uZWwgNjVQFJRDb25maWdb'
    b'MHgwMUZGMkJdIDwgOEABQIlQBZJSb3RhdGlvbiBEYXRhIFJhdGVQAYMCAitRAYFkUCWCSH'
    b'pREYEBUSGByFAVvlNldCBzYW1wbGUgcmF0ZSBmb3Igcm90YXRpb24gZGF0YSBmcm9tIDEg'
    b'dG8gMjAwIEh6LiBDaGFubmVsIDQ3UBSZQ29uZmlnWzB4MDFGRjJCXSAmIDIgPT0gMEAIQP'
    b'FQBaVJbnRlcm5hbCBUZW1wZXJhdHVyZS9QcmVzc3VyZSAoQ2ggMzYpQCdAxVEBgQNQAYMB'
    b'/yRQFfdFbmFibGUvRGlzYWJsZSBzbG93ZXIgaW50ZXJuYWwgZW52aXJvbm1lbnRhbCBzZW'
    b'5zb3JzLiBOT1RFOiBUZW1wZXJhdHVyZSBpcyByZXF1aXJlZCBmb3IgbWFpbiBhY2NlbGVy'
    b'b21ldGVyIG1lYXN1cmVtZW50c0EHnFAFmUVuYWJsZSBQcmVzc3VyZSAoQ2ggMzYuMClBB5'
    b'9QBZxFbmFibGUgVGVtcGVyYXR1cmUgKENoIDM2LjEpQAhAkFAFoENvbnRyb2wgUGFkIExp'
    b'Z2h0IFNlbnNvciAoQ2ggNzYpQCfqUAGDAf9MUBW+RW5hYmxlL0Rpc2FibGUgbGlnaHQgc2'
    b'Vuc29yIGF0IDQgSHogLSBOT1RFOiBESVNBQkxFRCBGT1IgQUxQSEFBB6BQBZ1FbmFibGUg'
    b'TGlnaHQgU2Vuc29yIChDaCA3Ni4wKUAPgEBPgEoIgEoogEpIgA=='
)
