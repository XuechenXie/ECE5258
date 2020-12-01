myFolder = './test_og';
filePattern = fullfile(myFolder, '*.jpg');
jpegFiles = dir(filePattern);
length(jpegFiles)
for k = 1:length(jpegFiles)
    baseFileName = jpegFiles(k).name;
    fullFileName = fullfile(myFolder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    img = imread(fullFileName);
    percentage = 0.75;
    targetSize = [round(size(img,1)*percentage) round(size(img,2)*percentage)];
    win1 = centerCropWindow2d(size(img),targetSize);
    B1 = imcrop(img,win1);
    fullFileName = fullfile('./test_crop', baseFileName);
    imwrite(B1, fullFileName);
end