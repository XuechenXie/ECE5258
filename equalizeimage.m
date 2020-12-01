myFolder = './train_grayscale';
filePattern = fullfile(myFolder, '*.jpg');
jpegFiles = dir(filePattern);
length(jpegFiles)
for k = 1:length(jpegFiles)
    baseFileName = jpegFiles(k).name;
    fullFileName = fullfile(myFolder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    img = imread(fullFileName);
    B1 = histeq(img);
    fullFileName = fullfile('./train_grayscale_equalization', baseFileName);
    imwrite(B1, fullFileName);
end