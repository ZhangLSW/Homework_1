obj-m:=myled.o
KERNEL:=/lib/modules/$(shell uname -r)/build

myled.ko:myled.c
        make -C $(KERNEL) M=`pwd` V=1 modules
clean:
        make -C $(KERNEL) M=`pwd` V=1 clean