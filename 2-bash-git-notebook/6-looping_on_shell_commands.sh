# Write loops to iterate over lists

# Loop example
for i in 1 2 3 4 5
do
  echo "Looping ... number $i"
done

# Same example, but now in one single line
for i in 1 2 3 4 5; do echo "Looping ... number $i"; done

# Looping over files
for f in ~/Desktop/* /tmp/*
do
	echo "Processing $f"
done