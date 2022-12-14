```C
  printf("Enter The Secret Code :  ");
  fgets(&local_28,0x14,stdin);
  printf("\nFlag: ");
  if (local_27 == 'D') {
    printf(">>");
    if (local_26 == 'D') {
      printf("YUCTF{T7is_is_n0t_T73_Fl4g}");
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
    if (local_26 == '\x01') {
      printf("YUC");
      if (local_25 != 'A') {
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      printf("TF{");
      if (local_23 != ' ') {
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      printf("N0t");
      if (local_22 != '!') {
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      printf("_T7");
      if (local_20 != 'e') {
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      printf("4t_");
      if (local_1f != '\x19') {
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      printf("74rd");
      if (local_1e != '\t') {
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      puts("}");
    }
  }
  return 0;
}

```
In each printf statement combined we can easy see the flag  :  YUCTF{N0t_T74t_74rd}
