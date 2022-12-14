A didn't find anything in the function but in the assembly view i found somthing interesting

```assembly
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined main()
             undefined         AL:1           <RETURN>
             undefined1        Stack[-0x15]:1 local_15                                XREF[1]:     00101175(W)  
             undefined1        Stack[-0x16]:1 local_16                                XREF[1]:     00101171(W)  
             undefined1        Stack[-0x17]:1 local_17                                XREF[1]:     0010116d(W)  
             undefined1        Stack[-0x18]:1 local_18                                XREF[1]:     00101169(W)  
             undefined1        Stack[-0x19]:1 local_19                                XREF[1]:     00101165(W)  
             undefined1        Stack[-0x1a]:1 local_1a                                XREF[1]:     00101161(W)  
             undefined1        Stack[-0x1b]:1 local_1b                                XREF[1]:     0010115d(W)  
             undefined1        Stack[-0x1c]:1 local_1c                                XREF[1]:     00101159(W)  
             undefined1        Stack[-0x1d]:1 local_1d                                XREF[1]:     00101155(W)  
             undefined1        Stack[-0x1e]:1 local_1e                                XREF[1]:     00101151(W)  
             undefined1        Stack[-0x1f]:1 local_1f                                XREF[1]:     0010114d(W)  
             undefined1        Stack[-0x20]:1 local_20                                XREF[1]:     00101149(W)  
             undefined1        Stack[-0x21]:1 local_21                                XREF[1]:     00101145(W)  
             undefined1        Stack[-0x22]:1 local_22                                XREF[1]:     00101141(W)  
             undefined1        Stack[-0x23]:1 local_23                                XREF[1]:     0010113d(W)  
             undefined1        Stack[-0x24]:1 local_24                                XREF[1]:     00101139(W)  
             undefined1        Stack[-0x25]:1 local_25                                XREF[1]:     00101135(W)  
             undefined1        Stack[-0x26]:1 local_26                                XREF[1]:     00101131(W)  
             undefined1        Stack[-0x27]:1 local_27                                XREF[1]:     0010112d(W)  
             undefined1        Stack[-0x28]:1 local_28                                XREF[1]:     00101129(W)  
                             main                                            XREF[4]:     Entry Point(*), 
                                                                                          _start:0010105d(*), 00102028, 
                                                                                          001020d0(*)  
        00101125 55              PUSH       RBP
        00101126 48 89 e5        MOV        RBP,RSP
        00101129 c6 45 e0 79     MOV        byte ptr [RBP + local_28],0x79
        0010112d c6 45 e1 75     MOV        byte ptr [RBP + local_27],0x75
        00101131 c6 45 e2 63     MOV        byte ptr [RBP + local_26],0x63
        00101135 c6 45 e3 74     MOV        byte ptr [RBP + local_25],0x74
        00101139 c6 45 e4 66     MOV        byte ptr [RBP + local_24],0x66
        0010113d c6 45 e5 7b     MOV        byte ptr [RBP + local_23],0x7b
        00101141 c6 45 e6 62     MOV        byte ptr [RBP + local_22],0x62
        00101145 c6 45 e7 34     MOV        byte ptr [RBP + local_21],0x34
        00101149 c6 45 e8 62     MOV        byte ptr [RBP + local_20],0x62
        0010114d c6 45 e9 79     MOV        byte ptr [RBP + local_1f],0x79
        00101151 c6 45 ea 5f     MOV        byte ptr [RBP + local_1e],0x5f
        00101155 c6 45 eb 72     MOV        byte ptr [RBP + local_1d],0x72
        00101159 c6 45 ec 33     MOV        byte ptr [RBP + local_1c],0x33
        0010115d c6 45 ed 76     MOV        byte ptr [RBP + local_1b],0x76
        00101161 c6 45 ee 5f     MOV        byte ptr [RBP + local_1a],0x5f
        00101165 c6 45 ef 66     MOV        byte ptr [RBP + local_19],0x66
        00101169 c6 45 f0 6c     MOV        byte ptr [RBP + local_18],0x6c
        0010116d c6 45 f1 34     MOV        byte ptr [RBP + local_17],0x34
        00101171 c6 45 f2 67     MOV        byte ptr [RBP + local_16],0x67
        00101175 c6 45 f3 7d     MOV        byte ptr [RBP + local_15],0x7d
        00101179 b8 00 00        MOV        EAX,0x0
                 00 00

```
As we can see we have a hex values.

then decode it in hex combined, the flag : yuctf{b4by_r3v_fl4g}
