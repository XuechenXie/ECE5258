myFolder = './test_og';
filePattern = fullfile(myFolder, '*.jpg');
jpegFiles = dir(filePattern);
length(jpegFiles)
for k = 1:length(jpegFiles)
    baseFileName = jpegFiles(k).name;
    fullFileName = fullfile(myFolder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    img = imread(fullFileName);
    if size(img,3)==3
        B1 = rgb2gray(img);
    else
        B1 = img;
    end
    fullFileName = fullfile('./train_grayscale', baseFileName);
    imwrite(B1, fullFileName);
end