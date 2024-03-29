import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Language


def populate_model(request):
    # The JSON data.
    data = """
    [
        {
            "code": "ab",
            "name": "Abkhaz",
            "nativeName": "\u0430\u04a7\u0441\u0443\u0430"
        },
        {
            "code": "aa",
            "name": "Afar",
            "nativeName": "Afaraf"
        },
        {
            "code": "af",
            "name": "Afrikaans",
            "nativeName": "Afrikaans"
        },
        {
            "code": "ak",
            "name": "Akan",
            "nativeName": "Akan"
        },
        {
            "code": "sq",
            "name": "Albanian",
            "nativeName": "Shqip"
        },
        {
            "code": "am",
            "name": "Amharic",
            "nativeName": "\u12a0\u121b\u122d\u129b"
        },
        {
            "code": "ar",
            "name": "Arabic",
            "nativeName": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
        },
        {
            "code": "an",
            "name": "Aragonese",
            "nativeName": "Aragon\u00e9s"
        },
        {
            "code": "hy",
            "name": "Armenian",
            "nativeName": "\u0540\u0561\u0575\u0565\u0580\u0565\u0576"
        },
        {
            "code": "as",
            "name": "Assamese",
            "nativeName": "\u0985\u09b8\u09ae\u09c0\u09af\u09bc\u09be"
        },
        {
            "code": "av",
            "name": "Avaric",
            "nativeName": "\u0430\u0432\u0430\u0440 \u043c\u0430\u0446\u04c0, \u043c\u0430\u0433\u04c0\u0430\u0440\u0443\u043b \u043c\u0430\u0446\u04c0"
        },
        {
            "code": "ae",
            "name": "Avestan",
            "nativeName": "avesta"
        },
        {
            "code": "ay",
            "name": "Aymara",
            "nativeName": "aymar aru"
        },
        {
            "code": "az",
            "name": "Azerbaijani",
            "nativeName": "az\u0259rbaycan dili"
        },
        {
            "code": "bm",
            "name": "Bambara",
            "nativeName": "bamanankan"
        },
        {
            "code": "ba",
            "name": "Bashkir",
            "nativeName": "\u0431\u0430\u0448\u04a1\u043e\u0440\u0442 \u0442\u0435\u043b\u0435"
        },
        {
            "code": "eu",
            "name": "Basque",
            "nativeName": "euskara, euskera"
        },
        {
            "code": "be",
            "name": "Belarusian",
            "nativeName": "\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f"
        },
        {
            "code": "bn",
            "name": "Bengali",
            "nativeName": "\u09ac\u09be\u0982\u09b2\u09be"
        },
        {
            "code": "bh",
            "name": "Bihari",
            "nativeName": "\u092d\u094b\u091c\u092a\u0941\u0930\u0940"
        },
        {
            "code": "bi",
            "name": "Bislama",
            "nativeName": "Bislama"
        },
        {
            "code": "bs",
            "name": "Bosnian",
            "nativeName": "bosanski jezik"
        },
        {
            "code": "br",
            "name": "Breton",
            "nativeName": "brezhoneg"
        },
        {
            "code": "bg",
            "name": "Bulgarian",
            "nativeName": "\u0431\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438 \u0435\u0437\u0438\u043a"
        },
        {
            "code": "my",
            "name": "Burmese",
            "nativeName": "\u1017\u1019\u102c\u1005\u102c"
        },
        {
            "code": "ca",
            "name": "Catalan; Valencian",
            "nativeName": "Catal\u00e0"
        },
        {
            "code": "ch",
            "name": "Chamorro",
            "nativeName": "Chamoru"
        },
        {
            "code": "ce",
            "name": "Chechen",
            "nativeName": "\u043d\u043e\u0445\u0447\u0438\u0439\u043d \u043c\u043e\u0442\u0442"
        },
        {
            "code": "ny",
            "name": "Chichewa; Chewa; Nyanja",
            "nativeName": "chiChe\u0175a, chinyanja"
        },
        {
            "code": "zh",
            "name": "Chinese",
            "nativeName": "\u4e2d\u6587 (Zh\u014dngw\u00e9n), \u6c49\u8bed, \u6f22\u8a9e"
        },
        {
            "code": "cv",
            "name": "Chuvash",
            "nativeName": "\u0447\u04d1\u0432\u0430\u0448 \u0447\u04d7\u043b\u0445\u0438"
        },
        {
            "code": "kw",
            "name": "Cornish",
            "nativeName": "Kernewek"
        },
        {
            "code": "co",
            "name": "Corsican",
            "nativeName": "corsu, lingua corsa"
        },
        {
            "code": "cr",
            "name": "Cree",
            "nativeName": "\u14c0\u1426\u1403\u152d\u140d\u140f\u1423"
        },
        {
            "code": "hr",
            "name": "Croatian",
            "nativeName": "hrvatski"
        },
        {
            "code": "cs",
            "name": "Czech",
            "nativeName": "\u010desky, \u010de\u0161tina"
        },
        {
            "code": "da",
            "name": "Danish",
            "nativeName": "dansk"
        },
        {
            "code": "dv",
            "name": "Divehi; Dhivehi; Maldivian;",
            "nativeName": "\u078b\u07a8\u0788\u07ac\u0780\u07a8"
        },
        {
            "code": "nl",
            "name": "Dutch",
            "nativeName": "Nederlands, Vlaams"
        },
        {
            "code": "en",
            "name": "English",
            "nativeName": "English"
        },
        {
            "code": "eo",
            "name": "Esperanto",
            "nativeName": "Esperanto"
        },
        {
            "code": "et",
            "name": "Estonian",
            "nativeName": "eesti, eesti keel"
        },
        {
            "code": "ee",
            "name": "Ewe",
            "nativeName": "E\u028begbe"
        },
        {
            "code": "fo",
            "name": "Faroese",
            "nativeName": "f\u00f8royskt"
        },
        {
            "code": "fj",
            "name": "Fijian",
            "nativeName": "vosa Vakaviti"
        },
        {
            "code": "fi",
            "name": "Finnish",
            "nativeName": "suomi, suomen kieli"
        },
        {
            "code": "fr",
            "name": "French",
            "nativeName": "fran\u00e7ais, langue fran\u00e7aise"
        },
        {
            "code": "ff",
            "name": "Fula; Fulah; Pulaar; Pular",
            "nativeName": "Fulfulde, Pulaar, Pular"
        },
        {
            "code": "gl",
            "name": "Galician",
            "nativeName": "Galego"
        },
        {
            "code": "ka",
            "name": "Georgian",
            "nativeName": "\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8"
        },
        {
            "code": "de",
            "name": "German",
            "nativeName": "Deutsch"
        },
        {
            "code": "el",
            "name": "Greek, Modern",
            "nativeName": "\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac"
        },
        {
            "code": "gn",
            "name": "Guaran\u00ed",
            "nativeName": "Ava\u00f1e\u1ebd"
        },
        {
            "code": "gu",
            "name": "Gujarati",
            "nativeName": "\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0"
        },
        {
            "code": "ht",
            "name": "Haitian; Haitian Creole",
            "nativeName": "Krey\u00f2l ayisyen"
        },
        {
            "code": "ha",
            "name": "Hausa",
            "nativeName": "Hausa, \u0647\u064e\u0648\u064f\u0633\u064e"
        },
        {
            "code": "he",
            "name": "Hebrew (modern)",
            "nativeName": "\u05e2\u05d1\u05e8\u05d9\u05ea"
        },
        {
            "code": "hz",
            "name": "Herero",
            "nativeName": "Otjiherero"
        },
        {
            "code": "hi",
            "name": "Hindi",
            "nativeName": "\u0939\u093f\u0928\u094d\u0926\u0940, \u0939\u093f\u0902\u0926\u0940"
        },
        {
            "code": "ho",
            "name": "Hiri Motu",
            "nativeName": "Hiri Motu"
        },
        {
            "code": "hu",
            "name": "Hungarian",
            "nativeName": "Magyar"
        },
        {
            "code": "ia",
            "name": "Interlingua",
            "nativeName": "Interlingua"
        },
        {
            "code": "id",
            "name": "Indonesian",
            "nativeName": "Bahasa Indonesia"
        },
        {
            "code": "ie",
            "name": "Interlingue",
            "nativeName": "Originally called Occidental; then Interlingue after WWII"
        },
        {
            "code": "ga",
            "name": "Irish",
            "nativeName": "Gaeilge"
        },
        {
            "code": "ig",
            "name": "Igbo",
            "nativeName": "As\u1ee5s\u1ee5 Igbo"
        },
        {
            "code": "ik",
            "name": "Inupiaq",
            "nativeName": "I\u00f1upiaq, I\u00f1upiatun"
        },
        {
            "code": "io",
            "name": "Ido",
            "nativeName": "Ido"
        },
        {
            "code": "is",
            "name": "Icelandic",
            "nativeName": "\u00cdslenska"
        },
        {
            "code": "it",
            "name": "Italian",
            "nativeName": "Italiano"
        },
        {
            "code": "iu",
            "name": "Inuktitut",
            "nativeName": "\u1403\u14c4\u1483\u144e\u1450\u1466"
        },
        {
            "code": "ja",
            "name": "Japanese",
            "nativeName": "\u65e5\u672c\u8a9e (\u306b\u307b\u3093\u3054\uff0f\u306b\u3063\u307d\u3093\u3054)"
        },
        {
            "code": "jv",
            "name": "Javanese",
            "nativeName": "basa Jawa"
        },
        {
            "code": "kl",
            "name": "Kalaallisut, Greenlandic",
            "nativeName": "kalaallisut, kalaallit oqaasii"
        },
        {
            "code": "kn",
            "name": "Kannada",
            "nativeName": "\u0c95\u0ca8\u0ccd\u0ca8\u0ca1"
        },
        {
            "code": "kr",
            "name": "Kanuri",
            "nativeName": "Kanuri"
        },
        {
            "code": "ks",
            "name": "Kashmiri",
            "nativeName": "\u0915\u0936\u094d\u092e\u0940\u0930\u0940, \u0643\u0634\u0645\u064a\u0631\u064a\u200e"
        },
        {
            "code": "kk",
            "name": "Kazakh",
            "nativeName": "\u049a\u0430\u0437\u0430\u049b \u0442\u0456\u043b\u0456"
        },
        {
            "code": "km",
            "name": "Khmer",
            "nativeName": "\u1797\u17b6\u179f\u17b6\u1781\u17d2\u1798\u17c2\u179a"
        },
        {
            "code": "ki",
            "name": "Kikuyu, Gikuyu",
            "nativeName": "G\u0129k\u0169y\u0169"
        },
        {
            "code": "rw",
            "name": "Kinyarwanda",
            "nativeName": "Ikinyarwanda"
        },
        {
            "code": "ky",
            "name": "Kirghiz, Kyrgyz",
            "nativeName": "\u043a\u044b\u0440\u0433\u044b\u0437 \u0442\u0438\u043b\u0438"
        },
        {
            "code": "kv",
            "name": "Komi",
            "nativeName": "\u043a\u043e\u043c\u0438 \u043a\u044b\u0432"
        },
        {
            "code": "kg",
            "name": "Kongo",
            "nativeName": "KiKongo"
        },
        {
            "code": "ko",
            "name": "Korean",
            "nativeName": "\ud55c\uad6d\uc5b4 (\u97d3\u570b\u8a9e), \uc870\uc120\ub9d0 (\u671d\u9bae\u8a9e)"
        },
        {
            "code": "ku",
            "name": "Kurdish",
            "nativeName": "Kurd\u00ee, \u0643\u0648\u0631\u062f\u06cc\u200e"
        },
        {
            "code": "kj",
            "name": "Kwanyama, Kuanyama",
            "nativeName": "Kuanyama"
        },
        {
            "code": "la",
            "name": "Latin",
            "nativeName": "latine, lingua latina"
        },
        {
            "code": "lb",
            "name": "Luxembourgish, Letzeburgesch",
            "nativeName": "L\u00ebtzebuergesch"
        },
        {
            "code": "lg",
            "name": "Luganda",
            "nativeName": "Luganda"
        },
        {
            "code": "li",
            "name": "Limburgish, Limburgan, Limburger",
            "nativeName": "Limburgs"
        },
        {
            "code": "ln",
            "name": "Lingala",
            "nativeName": "Ling\u00e1la"
        },
        {
            "code": "lo",
            "name": "Lao",
            "nativeName": "\u0e9e\u0eb2\u0eaa\u0eb2\u0ea5\u0eb2\u0ea7"
        },
        {
            "code": "lt",
            "name": "Lithuanian",
            "nativeName": "lietuvi\u0173 kalba"
        },
        {
            "code": "lu",
            "name": "Luba-Katanga",
            "nativeName": ""
        },
        {
            "code": "lv",
            "name": "Latvian",
            "nativeName": "latvie\u0161u valoda"
        },
        {
            "code": "gv",
            "name": "Manx",
            "nativeName": "Gaelg, Gailck"
        },
        {
            "code": "mk",
            "name": "Macedonian",
            "nativeName": "\u043c\u0430\u043a\u0435\u0434\u043e\u043d\u0441\u043a\u0438 \u0458\u0430\u0437\u0438\u043a"
        },
        {
            "code": "mg",
            "name": "Malagasy",
            "nativeName": "Malagasy fiteny"
        },
        {
            "code": "ms",
            "name": "Malay",
            "nativeName": "bahasa Melayu, \u0628\u0647\u0627\u0633 \u0645\u0644\u0627\u064a\u0648\u200e"
        },
        {
            "code": "ml",
            "name": "Malayalam",
            "nativeName": "\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02"
        },
        {
            "code": "mt",
            "name": "Maltese",
            "nativeName": "Malti"
        },
        {
            "code": "mi",
            "name": "M\u0101ori",
            "nativeName": "te reo M\u0101ori"
        },
        {
            "code": "mr",
            "name": "Marathi (Mar\u0101\u1e6dh\u012b)",
            "nativeName": "\u092e\u0930\u093e\u0920\u0940"
        },
        {
            "code": "mh",
            "name": "Marshallese",
            "nativeName": "Kajin M\u0327aje\u013c"
        },
        {
            "code": "mn",
            "name": "Mongolian",
            "nativeName": "\u043c\u043e\u043d\u0433\u043e\u043b"
        },
        {
            "code": "na",
            "name": "Nauru",
            "nativeName": "Ekakair\u0169 Naoero"
        },
        {
            "code": "nv",
            "name": "Navajo, Navaho",
            "nativeName": "Din\u00e9 bizaad, Din\u00e9k\u02bceh\u01f0\u00ed"
        },
        {
            "code": "nb",
            "name": "Norwegian Bokm\u00e5l",
            "nativeName": "Norsk bokm\u00e5l"
        },
        {
            "code": "nd",
            "name": "North Ndebele",
            "nativeName": "isiNdebele"
        },
        {
            "code": "ne",
            "name": "Nepali",
            "nativeName": "\u0928\u0947\u092a\u093e\u0932\u0940"
        },
        {
            "code": "ng",
            "name": "Ndonga",
            "nativeName": "Owambo"
        },
        {
            "code": "nn",
            "name": "Norwegian Nynorsk",
            "nativeName": "Norsk nynorsk"
        },
        {
            "code": "no",
            "name": "Norwegian",
            "nativeName": "Norsk"
        },
        {
            "code": "ii",
            "name": "Nuosu",
            "nativeName": "\ua188\ua320\ua4bf Nuosuhxop"
        },
        {
            "code": "nr",
            "name": "South Ndebele",
            "nativeName": "isiNdebele"
        },
        {
            "code": "oc",
            "name": "Occitan",
            "nativeName": "Occitan"
        },
        {
            "code": "oj",
            "name": "Ojibwe, Ojibwa",
            "nativeName": "\u140a\u14c2\u1511\u14c8\u142f\u14a7\u140e\u14d0"
        },
        {
            "code": "cu",
            "name": "Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic",
            "nativeName": "\u0469\u0437\u044b\u043a\u044a \u0441\u043b\u043e\u0432\u0463\u043d\u044c\u0441\u043a\u044a"
        },
        {
            "code": "om",
            "name": "Oromo",
            "nativeName": "Afaan Oromoo"
        },
        {
            "code": "or",
            "name": "Oriya",
            "nativeName": "\u0b13\u0b21\u0b3c\u0b3f\u0b06"
        },
        {
            "code": "os",
            "name": "Ossetian, Ossetic",
            "nativeName": "\u0438\u0440\u043e\u043d \u00e6\u0432\u0437\u0430\u0433"
        },
        {
            "code": "pa",
            "name": "Panjabi, Punjabi",
            "nativeName": "\u0a2a\u0a70\u0a1c\u0a3e\u0a2c\u0a40, \u067e\u0646\u062c\u0627\u0628\u06cc\u200e"
        },
        {
            "code": "pi",
            "name": "P\u0101li",
            "nativeName": "\u092a\u093e\u0934\u093f"
        },
        {
            "code": "fa",
            "name": "Persian",
            "nativeName": "\u0641\u0627\u0631\u0633\u06cc"
        },
        {
            "code": "pl",
            "name": "Polish",
            "nativeName": "polski"
        },
        {
            "code": "ps",
            "name": "Pashto, Pushto",
            "nativeName": "\u067e\u069a\u062a\u0648"
        },
        {
            "code": "pt",
            "name": "Portuguese",
            "nativeName": "Portugu\u00eas"
        },
        {
            "code": "qu",
            "name": "Quechua",
            "nativeName": "Runa Simi, Kichwa"
        },
        {
            "code": "rm",
            "name": "Romansh",
            "nativeName": "rumantsch grischun"
        },
        {
            "code": "rn",
            "name": "Kirundi",
            "nativeName": "kiRundi"
        },
        {
            "code": "ro",
            "name": "Romanian, Moldavian, Moldovan",
            "nativeName": "rom\u00e2n\u0103"
        },
        {
            "code": "ru",
            "name": "Russian",
            "nativeName": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a"
        },
        {
            "code": "sa",
            "name": "Sanskrit (Sa\u1e41sk\u1e5bta)",
            "nativeName": "\u0938\u0902\u0938\u094d\u0915\u0943\u0924\u092e\u094d"
        },
        {
            "code": "sc",
            "name": "Sardinian",
            "nativeName": "sardu"
        },
        {
            "code": "sd",
            "name": "Sindhi",
            "nativeName": "\u0938\u093f\u0928\u094d\u0927\u0940, \u0633\u0646\u068c\u064a\u060c \u0633\u0646\u062f\u06be\u06cc\u200e"
        },
        {
            "code": "se",
            "name": "Northern Sami",
            "nativeName": "Davvis\u00e1megiella"
        },
        {
            "code": "sm",
            "name": "Samoan",
            "nativeName": "gagana faa Samoa"
        },
        {
            "code": "sg",
            "name": "Sango",
            "nativeName": "y\u00e2ng\u00e2 t\u00ee s\u00e4ng\u00f6"
        },
        {
            "code": "sr",
            "name": "Serbian",
            "nativeName": "\u0441\u0440\u043f\u0441\u043a\u0438 \u0458\u0435\u0437\u0438\u043a"
        },
        {
            "code": "gd",
            "name": "Scottish Gaelic; Gaelic",
            "nativeName": "G\u00e0idhlig"
        },
        {
            "code": "sn",
            "name": "Shona",
            "nativeName": "chiShona"
        },
        {
            "code": "si",
            "name": "Sinhala, Sinhalese",
            "nativeName": "\u0dc3\u0dd2\u0d82\u0dc4\u0dbd"
        },
        {
            "code": "sk",
            "name": "Slovak",
            "nativeName": "sloven\u010dina"
        },
        {
            "code": "sl",
            "name": "Slovene",
            "nativeName": "sloven\u0161\u010dina"
        },
        {
            "code": "so",
            "name": "Somali",
            "nativeName": "Soomaaliga, af Soomaali"
        },
        {
            "code": "st",
            "name": "Southern Sotho",
            "nativeName": "Sesotho"
        },
        {
            "code": "es",
            "name": "Spanish; Castilian",
            "nativeName": "espa\u00f1ol, castellano"
        },
        {
            "code": "su",
            "name": "Sundanese",
            "nativeName": "Basa Sunda"
        },
        {
            "code": "sw",
            "name": "Swahili",
            "nativeName": "Kiswahili"
        },
        {
            "code": "ss",
            "name": "Swati",
            "nativeName": "SiSwati"
        },
        {
            "code": "sv",
            "name": "Swedish",
            "nativeName": "svenska"
        },
        {
            "code": "ta",
            "name": "Tamil",
            "nativeName": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd"
        },
        {
            "code": "te",
            "name": "Telugu",
            "nativeName": "\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41"
        },
        {
            "code": "tg",
            "name": "Tajik",
            "nativeName": "\u0442\u043e\u04b7\u0438\u043a\u04e3, to\u011fik\u012b, \u062a\u0627\u062c\u06cc\u06a9\u06cc\u200e"
        },
        {
            "code": "th",
            "name": "Thai",
            "nativeName": "\u0e44\u0e17\u0e22"
        },
        {
            "code": "ti",
            "name": "Tigrinya",
            "nativeName": "\u1275\u130d\u122d\u129b"
        },
        {
            "code": "bo",
            "name": "Tibetan Standard, Tibetan, Central",
            "nativeName": "\u0f56\u0f7c\u0f51\u0f0b\u0f61\u0f72\u0f42"
        },
        {
            "code": "tk",
            "name": "Turkmen",
            "nativeName": "T\u00fcrkmen, \u0422\u04af\u0440\u043a\u043c\u0435\u043d"
        },
        {
            "code": "tl",
            "name": "Tagalog",
            "nativeName": "Wikang Tagalog, \u170f\u1712\u1703\u1705\u1714 \u1706\u1704\u170e\u1713\u1704\u1714"
        },
        {
            "code": "tn",
            "name": "Tswana",
            "nativeName": "Setswana"
        },
        {
            "code": "to",
            "name": "Tonga (Tonga Islands)",
            "nativeName": "faka Tonga"
        },
        {
            "code": "tr",
            "name": "Turkish",
            "nativeName": "T\u00fcrk\u00e7e"
        },
        {
            "code": "ts",
            "name": "Tsonga",
            "nativeName": "Xitsonga"
        },
        {
            "code": "tt",
            "name": "Tatar",
            "nativeName": "\u0442\u0430\u0442\u0430\u0440\u0447\u0430, tatar\u00e7a, \u062a\u0627\u062a\u0627\u0631\u0686\u0627\u200e"
        },
        {
            "code": "tw",
            "name": "Twi",
            "nativeName": "Twi"
        },
        {
            "code": "ty",
            "name": "Tahitian",
            "nativeName": "Reo Tahiti"
        },
        {
            "code": "ug",
            "name": "Uighur, Uyghur",
            "nativeName": "Uy\u01a3urq\u0259, \u0626\u06c7\u064a\u063a\u06c7\u0631\u0686\u06d5\u200e"
        },
        {
            "code": "uk",
            "name": "Ukrainian",
            "nativeName": "\u0443\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430"
        },
        {
            "code": "ur",
            "name": "Urdu",
            "nativeName": "\u0627\u0631\u062f\u0648"
        },
        {
            "code": "uz",
            "name": "Uzbek",
            "nativeName": "zbek, \u040e\u0437\u0431\u0435\u043a, \u0623\u06c7\u0632\u0628\u06d0\u0643\u200e"
        },
        {
            "code": "ve",
            "name": "Venda",
            "nativeName": "Tshiven\u1e13a"
        },
        {
            "code": "vi",
            "name": "Vietnamese",
            "nativeName": "Ti\u1ebfng Vi\u1ec7t"
        },
        {
            "code": "vo",
            "name": "Volap\u00fck",
            "nativeName": "Volap\u00fck"
        },
        {
            "code": "wa",
            "name": "Walloon",
            "nativeName": "Walon"
        },
        {
            "code": "cy",
            "name": "Welsh",
            "nativeName": "Cymraeg"
        },
        {
            "code": "wo",
            "name": "Wolof",
            "nativeName": "Wollof"
        },
        {
            "code": "fy",
            "name": "Western Frisian",
            "nativeName": "Frysk"
        },
        {
            "code": "xh",
            "name": "Xhosa",
            "nativeName": "isiXhosa"
        },
        {
            "code": "yi",
            "name": "Yiddish",
            "nativeName": "\u05d9\u05d9\u05b4\u05d3\u05d9\u05e9"
        },
        {
            "code": "yo",
            "name": "Yoruba",
            "nativeName": "Yor\u00f9b\u00e1"
        },
        {
            "code": "za",
            "name": "Zhuang, Chuang",
            "nativeName": "Saɯ cueŋƅ, Saw cuengh"
        }]
    """

    # Load the data.
    data = json.loads(data)

    # Create a new instance of the model.
    model = Language()

    # Iterate through the data and populate the model.
    for language in data:
        try:
            # Get the existing model instance.
            existing_model = Language.objects.get(code=language["code"])
        except Language.DoesNotExist:
            # The model does not exist, so create a new one.
            existing_model = model

        # Update the model with the new data.
        existing_model.code = language["code"]
        existing_model.name = language["name"]
        existing_model.nativeName = language["nativeName"]
        existing_model.slug = language["code"]
        existing_model.status = "active"

        # Save the model.
        existing_model.save()

    # Return a success message.
    return HttpResponse("Model populated successfully.")
