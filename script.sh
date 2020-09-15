# enther path here
for OUTPUT in *.mp4;
do
	ffmpeg -i "$OUTPUT" 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,// >> output.txt;
done

python ./counter.py
rm output.txt