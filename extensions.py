FILE_EXTENSIONS = {

    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".svg", ".ico", ".tiff", ".heic",
        ".avif", ".tga", ".raw", ".cr2", ".nef",
        ".dng", ".orf", ".rw2", ".arw", ".raf",
        ".pef", ".erf", ".kdc", ".mrw", ".x3f"
    },

    "Videos": {
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm", ".mpeg", ".mpg", ".3gp",
        ".m4v", ".vob", ".ogv", ".rm", ".rmvb",
        ".mts", ".m2ts", ".ts", ".f4v"
    },

    "Audio": {
        ".mp3", ".wav", ".aac", ".flac", ".ogg",
        ".m4a", ".wma", ".aiff", ".mid",
        ".midi", ".opus", ".ape", ".alac",
        ".amr", ".caf", ".voc"
    },

    "Documents": {
        ".pdf", ".doc", ".docx", ".txt",
        ".rtf", ".odt", ".tex", ".md",
        ".wps", ".wpd", ".pages",
        ".epub", ".mobi", ".fb2", ".lit"
    },

    "Spreadsheets": {
        ".xls", ".xlsx", ".csv",
        ".ods", ".tsv", ".numbers",
        ".xlsm", ".xlsb"
    },

    "Presentations": {
        ".ppt", ".pptx", ".odp",
        ".key", ".pps", ".ppsx",
        ".pot", ".potx"
    },

    "Archives": {
        ".zip", ".rar", ".7z",
        ".tar", ".gz", ".bz2",
        ".xz", ".cab", ".tgz",
        ".tbz2", ".txz"
    },

    "Web": {
        ".html", ".htm", ".xhtml",
        ".css", ".scss", ".sass",
        ".less", ".js", ".mjs",
        ".cjs", ".ts", ".tsx",
        ".jsx", ".php", ".asp",
        ".aspx", ".jsp", ".graphql"
    },

    "Programming": {
        ".c", ".h",
        ".cpp", ".hpp", ".cc",
        ".java",
        ".go",
        ".rs",
        ".cs",
        ".swift",
        ".kt", ".kts",
        ".rb",
        ".pl",
        ".lua",
        ".dart",
        ".scala",
        ".r",".py", ".pyw", ".pyi"
    },

    "Scripts": {
        ".sh",
        ".bash",
        ".cmd",
        ".bat",
        ".ps1",
        ".vbs"
    },

    "Configuration": {
        ".env",
        ".ini",
        ".cfg",
        ".conf",
        ".config",
        ".yaml",
        ".yml",
        ".toml",
        ".dockerfile"
    },

    "Executables": {
        ".exe",
        ".msi",
        ".apk",
        ".deb",
        ".rpm",
        ".dmg",
        ".app",
        ".dll",
        ".sys",
        ".com",
        ".drv"
    },

    "Fonts": {
        ".ttf",
        ".otf",
        ".woff",
        ".woff2",
        ".eot"
    },

    "Databases": {
        ".db",
        ".sqlite",
        ".sqlite3",
        ".mdb",
        ".accdb"
    },
     "Security": {
        ".crt", ".cer", ".pem",
        ".key", ".csr",
        ".p12", ".pfx",
        ".der", ".jks",
        ".keystore", ".asc",
        ".gpg", ".sig",
        ".pub", ".p7b", ".p7c"
    },

    "Disk_Images": {
        ".iso", ".img",
        ".cue", ".mdf",
        ".mds", ".nrg",
        ".toast", ".daa",
        ".cdi"
    },

    "Data": {
        ".json", ".xml",
        ".bin", ".dat",
        ".sav", ".parquet",
        ".h5", ".hdf5",
        ".pickle", ".pkl",
        ".joblib", ".onnx",
        ".tflite", ".pb",
        ".ckpt", ".pth",
        ".safetensors"
    },

    "Logs": {
        ".log", ".err",
        ".out", ".trace",
        ".journal", ".history",
        ".dump"
    },

    "3D_Models": {
        ".3ds", ".obj",
        ".fbx", ".stl",
        ".dae", ".gltf",
        ".glb", ".blend",
        ".ply", ".x3d",
        ".3mf", ".usd",
        ".usdz"
    },

    "CAD": {
        ".dwg", ".dxf",
        ".dwt", ".step",
        ".stp", ".iges",
        ".igs", ".ipt",
        ".iam", ".idw",
        ".ipn", ".ifc",
        ".skp", ".rvt",
        ".rfa"
    },

    "Design": {
        ".psd", ".psb",
        ".ai", ".eps",
        ".indd", ".idml",
        ".cdr", ".xcf",
        ".fig", ".sketch",
        ".afdesign",
        ".afphoto",
        ".kra"
    },

    "GIS": {
        ".shp", ".shx",
        ".prj", ".kml",
        ".kmz", ".gpx",
        ".geojson", ".osm",
        ".ecw", ".sid",
        ".dem", ".bil",
        ".bsq", ".bip",
        ".qgs", ".qgz"
    },

    "Game_Files": {
        ".gam", ".pak",
        ".vpk", ".unity3d",
        ".bsp", ".nav",
        ".nbt", ".patch",
        ".mod", ".rom",
        ".wad", ".pk3",
        ".pk4", ".uasset",
        ".umap", ".arc",
        ".big", ".hog",
        ".lvl"
    },

    "Firmware": {
        ".fw", ".firmware",
        ".upd", ".bios",
        ".cap", ".fd",
        ".trx", ".chk",
        ".ofp", ".pac",
        ".nb0", ".kdz",
        ".tot"
    },

    "AI_ML": {
        ".pt", ".weights",
        ".cfgml", ".mlmodel"
    },

    "Medical": {
        ".dcm", ".dicom",
        ".nii", ".mha",
        ".mhd", ".hdr",
        ".ecg"
    },

    "Bioinformatics": {
        ".fasta", ".fa",
        ".fastq", ".fq",
        ".sam", ".bam",
        ".vcf", ".bcf",
        ".gff", ".gtf",
        ".bed"
    },

    "Virtual_Machines": {
        ".vdi", ".vmdk",
        ".vhd", ".vhdx",
        ".ova", ".ovf",
        ".qcow", ".qcow2",
        ".vbox", ".vmx",
        ".vmsd", ".vmsn"
    },

    "Apple": {
        ".ipa",
        ".plist",
        ".strings",
        ".mobileconfig",
        ".xcarchive",
        ".xcodeproj",
        ".xcworkspace",
        ".appex",
        ".framework"
    },
    "Android": {
        ".aab",
        ".dex",
        ".odex",
        ".vdex",
        ".arsc",
        ".obb"
    },

    "Adobe": {
        ".aep",
        ".aet",
        ".prproj",
        ".prel",
        ".lrtemplate",
        ".lrcat",
        ".xmp",
        ".abr",
        ".pat",
        ".atn",
        ".ase",
        ".acv",
        ".cff",
        ".fla",
        ".xfl",
        ".swf"
    },

    "Autodesk": {
        ".nwd",
        ".nwc",
        ".max",
        ".catpart",
        ".catproduct",
        ".cgr",
        ".jt",
        ".par"
    },

    "SolidWorks": {
        ".sldprt",
        ".sldasm",
        ".slddrw",
        ".sldlfp",
        ".sldmat",
        ".sldblk",
        ".sldbomtbt",
        ".sldreg",
        ".sldsetdoc"
    },

    "ANSYS": {
        ".cdb",
        ".rst",
        ".rth",
        ".emat",
        ".mode",
        ".full",
        ".esav"
    },

    "Electronics": {
        ".sch",
        ".brd",
        ".pcb",
        ".kicad_pcb",
        ".kicad_sch",
        ".dsn",
        ".gbr",
        ".gerber",
        ".drl",
        ".net"
    },

    "Robotics": {
        ".urdf",
        ".xacro",
        ".sdf",
        ".bag",
        ".world",
        ".launch",
        ".rviz",
        ".proto"
    },

    "Networking": {
        ".pcap",
        ".pcapng",
        ".cap",
        ".netxml",
        ".nmap",
        ".har",
        ".pkt",
        ".snoop",
        ".tr1"
    },

    "Servers": {
        ".service",
        ".socket",
        ".target",
        ".mount",
        ".timer",
        ".path",
        ".unit",
        ".cnf",
        ".htaccess",
        ".htpasswd"
    },

    "Cloud": {
        ".tf",
        ".tfvars",
        ".bicep",
        ".arm",
        ".pulumi",
        ".nomad",
        ".helm"
    },

    "Office_Legacy": {
        ".pub",
        ".vsd",
        ".one",
        ".xlt",
        ".pot"
    },

    "Broadcast": {
        ".dvr-ms",
        ".wtv",
        ".rec",
        ".264",
        ".265",
        ".h264",
        ".h265"
    },

    "Camera_RAW": {
        ".cr3",
        ".nrw",
        ".srf",
        ".sr2",
        ".iiq",
        ".3fr",
        ".fff",
        ".mos",
        ".rwl",
        ".gpr"
    },

    "Ebooks": {
        ".azw",
        ".azw3",
        ".ibooks",
        ".cbz",
        ".cbr",
        ".chm",
        ".opf",
        ".prc"
    },

    "Legacy_Formats": {
        ".wk1",
        ".wk3",
        ".wks",
        ".arj",
        ".lzh",
        ".zoo",
        ".pit",
        ".uc2",
        ".ha",
        ".sqz",
        ".yz1",
        ".hpk"
    },

    "Unreal_Engine": {
        ".uproject",
        ".uplugin",
        ".uasset",
        ".umap",
        ".ubulk",
        ".uexp",
        ".utoc",
        ".ucas",
        ".locres",
        ".locmeta"
    },

    "Unity_Internal": {
        ".unity",
        ".prefab",
        ".asset",
        ".anim",
        ".controller",
        ".mat",
        ".physicmaterial",
        ".terrainlayer",
        ".spriteatlas",
        ".unitypackage"
    },

    "CryEngine": {
        ".cry",
        ".cgf",
        ".chr",
        ".caf",
        ".mtl",
        ".pak2",
        ".soc",
        ".ly"
    },

    "Source_Engine": {
        ".vmt",
        ".vtf",
        ".mdl",
        ".phy",
        ".vtx",
        ".ani",
        ".ain",
        ".res"
    },

    "Frostbite": {
        ".toc",
        ".sb",
        ".cas",
        ".chunk",
        ".layout",
        ".ebx",
        ".itexture"
    },

    "PlayStation": {
        ".pbp",
        ".pkg",
        ".self",
        ".sprx",
        ".edat",
        ".sfo",
        ".psv",
        ".vmp",
        ".rif"
    },

    "Nintendo": {
        ".nds",
        ".3dsx",
        ".cia",
        ".nsp",
        ".xci",
        ".wad",
        ".dol",
        ".gcm",
        ".wbfs",
        ".rvz"
    },

    "Xbox": {
        ".xex",
        ".xbe",
        ".god",
        ".xvc",
        ".xcp"
    },

    "Sega": {
        ".gdi",
        ".32x",
        ".gg",
        ".sms",
        ".sg"
    },

    "Emulators": {
        ".state",
        ".srm",
        ".fcs",
        ".z64",
        ".n64",
        ".nes",
        ".gba",
        ".gbc",
        ".gb",
        ".gen"
    },

    "Linux_Kernel": {
        ".ko",
        ".initramfs",
        ".dtb",
        ".dtbo",
        ".configkernel",
        ".kallsyms"
    },

    "Reverse_Engineering": {
        ".idb",
        ".i64",
        ".til",
        ".smali",
        ".baksmali",
        ".lst",
        ".id0",
        ".id1",
        ".nam",
        ".tilib"
    },

    "Digital_Forensics": {
        ".e01",
        ".ex01",
        ".dd",
        ".aff",
        ".aff4",
        ".ad1",
        ".l01",
        ".mem"
    },

    "Malware_Analysis": {
        ".yar",
        ".yara",
        ".cuckoo",
        ".cape",
        ".hsb",
        ".ioc"
    },

    "Cryptocurrency_Blockchain": {
        ".wallet",
        ".keystore",
        ".seed",
        ".mnemonic",
        ".blk",
        ".ldb",
        ".sst",
        ".chain",
        ".rlp",
        ".trie"
    },

    "Siemens_NX": {
        ".prt",
        ".prt1",
        ".sim",
        ".fem",
        ".pax",
        ".dfa",
        ".dpv",
        ".afm"
    },

    "CATIA": {
        ".catdrawing",
        ".catshape",
        ".catalog",
        ".cgrmodel",
        ".catprocess",
        ".catanalysis"
    },

    "Blender_Internal": {
        ".bphys",
        ".blend1",
        ".blend2",
        ".btx",
        ".cache",
        ".blend.gz"
    },

    "Houdini": {
        ".hip",
        ".hiplc",
        ".hipnc",
        ".bgeo",
        ".bgeo.sc",
        ".simdata",
        ".otl",
        ".hda"
    },

    "Maya": {
        ".mb",
        ".ma",
        ".mel",
        ".atom",
        ".iff",
        ".mayaascii",
        ".mayabinary"
    },

    "GIS_Professional": {
        ".mxd",
        ".lyr",
        ".lyrx",
        ".sd",
        ".sde",
        ".gpkg",
        ".tab",
        ".mif",
        ".mid"
    },

    "Weather_Aviation": {
        ".bufr",
        ".grib2",
        ".metar",
        ".taf",
        ".sigwx",
        ".airac",
        ".sidproc",
        ".starproc"
    },

    "FPGA": {
        ".sof",
        ".pof",
        ".qpf",
        ".qsf",
        ".svf",
        ".jed",
        ".bit",
        ".mcs",
        ".ngc",
        ".ngd"
    },

    "PLC": {
        ".awl",
        ".scl",
        ".st",
        ".fbd",
        ".lad",
        ".l5k",
        ".l5x",
        ".ap14",
        ".rss"
    },

    "Medical_Imaging": {
        ".nrrd",
        ".nhdr",
        ".mnc",
        ".mgz",
        ".mgz2",
        ".vtkimg",
        ".mgz.gz"
    },

    "Spectroscopy": {
        ".sp",
        ".jdx",
        ".dx",
        ".fid",
        ".ser",
        ".mnova",
        ".mnv"
    },

    "Quantum_Chemistry": {
        ".gjc",
        ".fchk",
        ".chk",
        ".wfn",
        ".wfx",
        ".molden",
        ".cube",
        ".orca"
    },

    "Virtual_Reality": {
        ".vrscene",
        ".vrimg",
        ".vrmap",
        ".vrmesh",
        ".ovrscene",
        ".xrs"
    },

    "Legacy_Operating_Systems": {
        ".lnk16",
        ".pif",
        ".hlp",
        ".gid",
        ".386",
        ".fon2",
        ".drv16",
        ".ovl"
    },

    "Misc_Rare": {
        ".torrent",
        ".magnet",
        ".ics",
        ".vcfcard",
        ".emlx",
        ".mbox",
        ".pst",
        ".ost",
        ".pkpass",
        ".crdownload",
        ".part",
        ".download"
    },
     "Cisco": {
        ".ios", ".pkt", ".gns3",
        ".net", ".acl", ".cef", ".eem",
        ".lic", ".spa", ".pkg", ".conf"
    },

    "Juniper": {
        ".jcfg", ".junos", ".set",
        ".xmlconf", ".slax", ".op",
        ".xnm", ".jkscfg"
    },

    "MikroTik": {
        ".backup", ".rsc", ".npk",
        ".dude", ".keymik", ".routeros"
    },

    "Huawei": {
        ".vrp", ".cc", ".cfgbak",
        ".datcfg", ".hwlic", ".hwpkg"
    },

    "Oracle": {
        ".dmp", ".ctl", ".ora",
        ".par", ".trc", ".aud",
        ".rman", ".spfile"
    },

    "SQL_Server": {
        ".mdf", ".ndf", ".ldf",
        ".bacpac", ".dacpac",
        ".trn", ".sqlaudit"
    },

    "PostgreSQL": {
        ".pgsql", ".pgdump",
        ".pgpass", ".pgdata",
        ".pgwal", ".pgcontrol"
    },

    "MongoDB": {
        ".bson", ".wt",
        ".metadata", ".mongodump",
        ".oplog"
    },

    "Redis": {
        ".rdb", ".aof"
    },

    "Apache_Spark": {
        ".parquet", ".orc",
        ".avro", ".delta",
        ".spark", ".snappy"
    },

    "Hadoop": {
        ".seq", ".mapfile",
        ".hfile", ".crc",
        ".index"
    },

    "MATLAB": {
        ".mlx", ".slx",
        ".mdl", ".figmat",
        ".mexw64", ".mexa64",
        ".mexmaci64"
    },

    "Mathematica": {
        ".nb", ".cdfmath",
        ".mx", ".wl",
        ".wls", ".m"
    },

    "LabVIEW": {
        ".vi", ".ctl",
        ".lvclass", ".lvlib",
        ".lvproj", ".aliases",
        ".lvm"
    },

    "R_Studio": {
        ".rds", ".rdata",
        ".rhistory", ".rprofile",
        ".rnw", ".rmd"
    }
    
}