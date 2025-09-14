import pdf2html from 'pdf2html';
import fs from 'fs';

// // From file path
// const html1 = await pdf2html.html('b.pdf');
// console.log(html1);
// fs.writeFileSync('b.html', html1);

// // From buffer
// const pdfBuffer = fs.readFileSync('b.pdf');
// const html2 = await pdf2html.html(pdfBuffer);
// console.log(html2);
// fs.writeFileSync('b.html', html2);

// With options
const pdfBuffer = fs.readFileSync('b.pdf');
const html3 = await pdf2html.html(pdfBuffer, {
  maxBuffer: 1024 * 1024 * 10, // 10MB buffer
});
console.log(html3);
fs.writeFileSync('b.html', html3);
