"""
Default ConfigUI for W8-E100D40 data recorders 
"""

from base64 import b64decode

DEFAULT_CONFIG_UI = b64decode(
    b'd3dZHEAoSDxQBYdHZW5lcmFsQAXzUAWLRGV2aWNlIE5hbWVQAYMI/39RJIFAUBXYQSBjdX'
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
    b'ZyBmaWxlcy5AL4BAGEIIUAWMRW5hYmxlIFdpLUZpUAGDGP9/UQGBAUAn7FABgxn/f1EBgQ'
    b'FBB6lQBaZVcGxvYWQgcmVjb3JkaW5nIHRvIGNsb3VkIGFmdGVyIGZpbmlzaFAVs1NlbGVj'
    b'dCB0byB1cGxvYWQgZWFjaCBmaWxlIHdoZW4gcmVjb3JkaW5nIGNvbXBsZXRlc0AnQLZQAY'
    b'Ma/39RAYEAQQejUAWgRGVsZXRlIGZyb20gc3RvcmFnZSBhZnRlciB1cGxvYWRQFUCCUmVj'
    b'b3JkaW5nIGZpbGUgd2lsbCBiZSBkZWxldGVkIGFmdGVyIGEgc3VjY2Vzc2Z1bCB1cGxvYW'
    b'QsIGFuZCBtb3ZlZCB0byBhIHN1YmZvbGRlciBsYWJlbGVkICdmYWlsZWQnIGluIHRoZSBj'
    b'YXNlIG9mIGEgZmFpbGVkIHVwbG9hZEAnQMJQAYMd/39RAYEAQQepUAWmS2VlcCB0aGUgV2'
    b'ktRmkgbW9kdWxlIG9uIGFuZCBjb25uZWN0ZWRQFUCISWYgY2hlY2tlZCwgdGhlIFdpLUZp'
    b'IG1vZHVsZSB3aWxsIHN0YXkgb24gYW5kIGNvbm5lY3RlZC4gIEFsbG93cyBmb3IgZmFzdG'
    b'VyIHVwbG9hZCB0aW1lcyB3aXRoIHRoZSBleHBlbnNlIG9mIGluY3JlYXNlZCBwb3dlciBj'
    b'b25zdW1wdGlvbkAPgEBPgEAoSOhQBYhUcmlnZ2Vyc0AHQNpQBYxUcmlnZ2VyIE1vZGVQAY'
    b'MS/39RAYEAUBVAj0RlbGF5IFRoZW4gVHJpZ2dlcjogV2FpdCBzcGVjaWZpZWQgdGltZSwg'
    b'dGhlbiB3YWl0IGZvciB0cmlnZ2VyCkRlbGF5IE9yIFRyaWdnZXI6IEFjcXVpcmUgYWZ0ZX'
    b'Igd2FpdCBvciBvbiB0cmlnZ2VyLiBCYXR0ZXJ5IGxpZmUgbWF5IGJlIHJlZHVjZWQuQQeV'
    b'UAWSRGVsYXkgVGhlbiBUcmlnZ2VyQQeTUAWQRGVsYXkgT3IgVHJpZ2dlckAy9FAFjVN0YX'
    b'J0IGF0IFRpbWVQAYMP/39QFdtXYWl0IHVudGlsIHNldCB0aW1lIGJlZm9yZSBldmFsdWF0'
    b'aW5nIG90aGVyIHRyaWdnZXIgY29uZGl0aW9ucywgaW5jbHVkaW5nIGEgcmVjb3JkaW5nIG'
    b'RlbGF5QBGuUAWUUmVjb3JkaW5nIFRpbWUgTGltaXRQAYMN/39RIYT////wUCWHU2Vjb25k'
    b'c0ARQJBQBZhSZWNvcmRpbmcgRGVsYXkvSW50ZXJ2YWxQAYMM/39RAYEAUCWHU2Vjb25kc1'
    b'EhgwFRgFAV2FRpbWUgYmVmb3JlIHN0YXJ0aW5nIGEgcmVjb3JkaW5nLCBhbmQgdGltZSBi'
    b'ZXR3ZWVuIHJlY29yZGluZ3MgaWYgJ1JldHJpZ2dlcicgaXMgY2hlY2tlZC5AEa9QBZlSZW'
    b'NvcmRpbmcgRmlsZSBTaXplIExpbWl0UAGDEf9/USGE////8FAlg0tpQkAQQJdQBYlSZXRy'
    b'aWdnZXJQAYMO/39QFLBDb25maWdbMHhERkY3Rl09PW51bGwgYW5kIENvbmZpZ1sweDExRk'
    b'Y3Rl09PW51bGxQFc9XaGVuIHNldCwgU2xhbSBTdGljayB3aWxsIHJlLWFybSBhZnRlciBy'
    b'ZWNvcmRpbmcgdGltZSBvciBzaXplIGxpbWl0IGlzIHJlYWNoZWQuQBBAqFAFnldhaXQgZm'
    b'9yIEFsbCBTZW5zb3IgQ29uZGl0aW9uc1ABgxP/f1AV/ldoZW4gc2V0LCByZWNvcmRpbmcg'
    b'd2lsbCBvbmx5IHN0YXJ0IHdoZW4gYWxsIHRyaWdnZXJzIGFyZSBtZXQsIG90aGVyd2lzZS'
    b'ByZWNvcmRpbmcgd2lsbCBzdGFydCB3aGVuIGFueSBzZW5zb3IgY29uZGl0aW9uIGlzIG1l'
    b'dEAYQO5QBZBQcmVzc3VyZSBUcmlnZ2VyUAGDBQAkUQCBAECC5VAFlVByZXNzdXJlIFRyaW'
    b'dnZXIsIExvd1ABgwMAJFEBgwFfkFAlglBhUSGDAdTAUBWzU2V0IHRvIHN0YXJ0IHNhbXBs'
    b'aW5nIHdoZW4gb3V0c2lkZSBwcmVzc3VyZSB3aW5kb3cuQILmUAWWUHJlc3N1cmUgVHJpZ2'
    b'dlciwgSGlnaFABgwQAJFEBgwGtsFAlglBhUSGDAdTAUBWzU2V0IHRvIHN0YXJ0IHNhbXBs'
    b'aW5nIHdoZW4gb3V0c2lkZSBwcmVzc3VyZSB3aW5kb3cuQBhA+1AFk1RlbXBlcmF0dXJlIF'
    b'RyaWdnZXJQAYMFASRRAIEAQGPqUAWYVGVtcGVyYXR1cmUgVHJpZ2dlciwgTG93UAGDAwEk'
    b'UQKB9lAlgUNREoHYUSKBUFAVtlNldCB0byBzdGFydCBzYW1wbGluZyB3aGVuIG91dHNpZG'
    b'UgdGVtcGVyYXR1cmUgd2luZG93LkBj61AFmVRlbXBlcmF0dXJlIFRyaWdnZXIsIEhpZ2hQ'
    b'AYMEASRRAoEjUCWBQ1ESgdhRIoFQUBW2U2V0IHRvIHN0YXJ0IHNhbXBsaW5nIHdoZW4gb3'
    b'V0c2lkZSB0ZW1wZXJhdHVyZSB3aW5kb3cuQBhBqFAFm0FjY2VsZXJhdGlvbiBUcmlnZ2Vy'
    b'ICgxMDBnKVABgwX/CFARgwf/IFEAgQBQJIBQFJVDb25maWdbMHgwMUZGMDhdID09IDBAQ0'
    b'CrUROIwFkAAAAAAABRI4hAWQAAAAAAAFAFmUFjY2VsZXJhdGlvbiBUcmlnZ2VyLCBMb3dQ'
    b'AYMD/whRAoL5mlAV4EhpZ2ggcG93ZXIgdHJpZ2dlciB3aXRoIHByZS10cmlnZ2VyIGRhdG'
    b'EuIE5vdCByZWNvbW1lbmRlZCBmb3IgbG9uZyB3YWl0cyB3aXRob3V0IGV4dGVybmFsIHBv'
    b'd2VyLlIDiD9pABkAGQAZQENArFETiMBZAAAAAAAAUSOIQFkAAAAAAABQBZpBY2NlbGVyYX'
    b'Rpb24gVHJpZ2dlciwgSGlnaFABgwT/CFECggZmUBXgSGlnaCBwb3dlciB0cmlnZ2VyIHdp'
    b'dGggcHJlLXRyaWdnZXIgZGF0YS4gTm90IHJlY29tbWVuZGVkIGZvciBsb25nIHdhaXRzIH'
    b'dpdGhvdXQgZXh0ZXJuYWwgcG93ZXIuUgOIP2kAGQAZABlAGEGjUAWaQWNjZWxlcmF0aW9u'
    b'IFRyaWdnZXIgKDQwZylQAYMH/1BQFdRMb3cgcG93ZXIgdHJpZ2dlciB1c2luZyBkaWdpdG'
    b'FsIGFjY2VsZXJvbWV0ZXIgd2l0aCBEQyByZXNwb25zZS4gTm8gcHJlLXRyaWdnZXIgZGF0'
    b'YS5RAIEAUBGDBf8IUBGDB/8gUCSAUBSUQ29uZmlnWzB4MWZmNTBdID09IDBAQ0CyUAWWQW'
    b'NjZWxlcmF0aW9uIFRocmVzaG9sZFABgwT/UFEBgiAAUgOIP0QAFAAUABRRI4hARAAAAAAA'
    b'AFETgFAV8kxvdyBwb3dlciB0cmlnZ2VyLiBUaGUgbWluaW11bSBhY2NlbGVyYXRpb24gKH'
    b'Bvc2l0aXZlIG9yIG5lZ2F0aXZlKSB0byB0cmlnZ2VyIGEgcmVjb3JkaW5nLiBNdXN0IGJl'
    b'IGdyZWF0ZXIgdGhhbiAwLkAnxlABgwX/UFEBgQdBB5FQBY5YIEF4aXMgVHJpZ2dlckEHkV'
    b'AFjlkgQXhpcyBUcmlnZ2VyQQeRUAWOWiBBeGlzIFRyaWdnZXJAD4BAT4BAKEfjUAWMTWVh'
    b'c3VyZW1lbnRzQAhCW1AFmDEwMGcgQWNjZWxlcmF0aW9uIChDaCA4KVAkgEAnQJtRAYEPUA'
    b'GDAf8IUBWgRW5hYmxlL0Rpc2FibGUgYWNjZWxlcmF0aW9uIGF4ZXNBB5hQBZFFbmFibGUg'
    b'WCAoQ2ggOC4wKVEBgQBBB5hQBZFFbmFibGUgWSAoQ2ggOC4xKVEBgQFBB5hQBZFFbmFibG'
    b'UgWiAoQ2ggOC4yKVEBgQJBB5pQBZNFbmFibGUgTWljIChDaCA4LjMpUQGBA0ARQJpQBYtT'
    b'YW1wbGUgUmF0ZVABgwL/CFAV2FNldCBtYWluIGFjY2VsZXJhdGlvbiBzYW1wbGUgcmF0ZS'
    b'Bmcm9tIDEwIHRvIDIwMDAwIEh6LgpIaWdoZXIgcmF0ZSByZWR1Y2VzIGJhdHRlcnkgbGlm'
    b'ZS5QFJVDb25maWdbMHgwMUZGMDhdID09IDBRAYITiFAlgkh6URGBClEhgk4gQBFA/FAFo0'
    b'92ZXJyaWRlIEFudGlhbGlhc2luZyBGaWx0ZXIgQ3V0b2ZmUAGDCP8IUQGCA+hQJYJIelEh'
    b'gmGoUBVApURlZmF1bHQsIHdoZW4gbm90IGNoZWNrZWQsIG9mIG9uZS1maWZ0aCBzYW1wbG'
    b'UgZnJlcXVlbmN5LiBDdXQtb2ZmIGZyZXF1ZW5jeSBoYXMgMjklIGF0dGVudWF0aW9uLgo1'
    b'dGggb3JkZXIgQnV0dGVyd29ydGguIFNvbWUgYXR0ZW51YXRpb24gYXQgNjAlIG9mIGN1dC'
    b'1vZmYgZnJlcXVlbmN5LlAUlUNvbmZpZ1sweDAxRkYwOF0gPT0gMEAIQRxQBZs0MGcgREMg'
    b'QWNjZWxlcmF0aW9uIChDaCA4MClAJ59QAYMB/1BRAYEBQQeSUAWPRW5hYmxlIEFsbCBBeG'
    b'VzQBdA2FAFi1NhbXBsZSBSYXRlUAGDAv9QUQGCAfRQJYJIelAV3kxvdyBwYXNzIGZpbHRl'
    b'ciBpcyBzZXQgdG8gMjUlIG9mIGRhdGEgcmF0ZSwgc28gYSBkYXRhIHJhdGUgb2YgMjAwME'
    b'h6IGhhcyBhIExQIGZpbHRlciBhdCA1MDAgSHpQFJNub3QgQ29uZmlnWzB4MWZmNTBdQQeF'
    b'UQGCD6BBB4VRAYIH0EEHhVEBggPoQQeFUQGCAfRBB4RRAYH6QQeEUQGBfUEHhFEBgT9BB4'
    b'RRAYEgQQeEUQGBEEAIQTBQBahDb250cm9sIFBhZCBUZW1wZXJhdHVyZS9QcmVzc3VyZSAo'
    b'Q2ggNTkpQCdAm1EBgQNQAYMB/ztQFaVFbmFibGUvRGlzYWJsZSBzZW5zb3JzIG9uIGNvbn'
    b'Ryb2wgcGFkQQecUAWZRW5hYmxlIFByZXNzdXJlIChDaCA1OS4wKUEHn1AFnEVuYWJsZSBU'
    b'ZW1wZXJhdHVyZSAoQ2ggNTkuMSlBB6VQBaJFbmFibGUgUmVsYXRpdmUgSHVtaWRpdHkgKE'
    b'NoIDU5LjIpQBHjUAWLU2FtcGxlIFJhdGVQAYMC/ztQFJRDb25maWdbMHgxZmYzQl0gPT0g'
    b'MFAVpFNldCBzYW1wbGUgZnJlcXVlbmN5IGZyb20gMSB0byAxMCBIelEBgQpQJYJIelERgQ'
    b'FRIYEKQAhBzVAFmUluZXJ0aWFsIE1lYXN1cmVtZW50IFVuaXRAB0CWUAWQQWNxdWlzaXRp'
    b'b24gTW9kZVABgwH/K1AlgSBRAYEQQQeKUAWDT2ZmUQGBAEEHqFAFoUFic29sdXRlIE9yaW'
    b'VudGF0aW9uIChRdWF0ZXJuaW9uKVEBgQhBB6hQBaFSZWxhdGl2ZSBPcmllbnRhdGlvbiAo'
    b'UXVhdGVybmlvbilRAYEQQQePUAWIUm90YXRpb25RAYECQAFAhlAFlU9yaWVudGF0aW9uIE'
    b'RhdGEgUmF0ZVABgwIIK1EBgWRQJYJIelERgQFRIYHIUBW9U2FtcGxlIHJhdGUgZm9yIGRp'
    b'cmVjdGlvbmFsIGRhdGEgZnJvbSAxIHRvIDIwMCBIei4gQ2hhbm5lbCA2NVAUlENvbmZpZ1'
    b'sweDAxRkYyQl0gPCA4QAFAiVAFklJvdGF0aW9uIERhdGEgUmF0ZVABgwICK1EBgWRQJYJI'
    b'elERgQFRIYHIUBW+U2V0IHNhbXBsZSByYXRlIGZvciByb3RhdGlvbiBkYXRhIGZyb20gMS'
    b'B0byAyMDAgSHouIENoYW5uZWwgNDdQFJlDb25maWdbMHgwMUZGMkJdICYgMiA9PSAwQAhA'
    b'kFAFoENvbnRyb2wgUGFkIExpZ2h0IFNlbnNvciAoQ2ggNzYpQCfqUAGDAf9MUBW+RW5hYm'
    b'xlL0Rpc2FibGUgbGlnaHQgc2Vuc29yIGF0IDQgSHogLSBOT1RFOiBESVNBQkxFRCBGT1Ig'
    b'QUxQSEFBB6BQBZ1FbmFibGUgTGlnaHQgU2Vuc29yIChDaCA3Ni4wKUAIQLJQBZNCTUcyNT'
    b'AgR3lybyAoQ2ggODQpQCefUAGDAf9UUQGBAEEHklAFj0VuYWJsZSBBbGwgQXhlc0AX91AF'
    b'i1NhbXBsZSBSYXRlUAGDAv9UUQGCAZBQJYJIelAUk25vdCBDb25maWdbMHgxZmY1NF1BB4'
    b'VRAYIMgEEHhVEBggZAQQeFUQGCAyBBB4VRAYIBkEEHhFEBgchBB4RRAYFkQQeEUQGBMkEH'
    b'hFEBgRlBB4RRAYEMQA+AQE+ASgiASiiASkiA'
)