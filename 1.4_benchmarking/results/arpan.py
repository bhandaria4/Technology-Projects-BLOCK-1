dd if=/dev/zero of=testfile.bin bs=100M count=1 oflag=direct

dd if=testfile.bin of=/dev/null bs=100M count=1 ifflag=direct
