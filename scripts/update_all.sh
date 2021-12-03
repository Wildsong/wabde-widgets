for d in *; do
    if [ -d $d ]; then
	cd $d
	echo $d
	git checkout main
	grep version manifest.json
	cd ..
    fi
done
