#<mark>**Projede İstenenler:**</mark> 
##<mark>**İngilizce:**</mark>
-Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
_**Rules**_

1. Liste Elemanı The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.
 Situations that will return an error:
2. Liste Elemanı If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
3. Liste Elemanı The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
4. Liste Elemanı Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
5. Liste Elemanı Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
6. Liste Elemanı If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
7. Liste Elemanı Numbers should be right-aligned.
8. Liste Elemanı There should be four spaces between each problem.
9. Liste Elemanı There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
-Note: open the browser console with F12 to see a more verbose output of the tests.
##<mark>**Türkçe:**</mark>
-Aritmetik problemleri olan dizelerin listesini alan aritmetik_arranger fonksiyonunu bitirin ve problemleri dikey ve yan yana düzenlenmiş olarak döndürün. Fonksiyon isteğe bağlı olarak ikinci bir argüman almalıdır. İkinci bağımsız değişken Doğru olarak ayarlandığında yanıtlar görüntülenmelidir.
**_Kurallar:_**
1. Liste ElemanıSağlanan problemler doğru şekilde biçimlendirilmişse işlev doğru dönüşümü döndürür, aksi takdirde kullanıcı için anlamlı olan bir hatayı tanımlayan bir dize döndürür.
Hata döndürecek durumlar:
 2. Liste Elemanı İşleve sağlanan çok fazla sorun varsa. Sınır beştir, daha fazlası geri dönecektir: 'Hata: Çok fazla sorun var.'
3. Liste Elemanı Fonksiyonun kabul edeceği uygun operatörler toplama ve çıkarmadır. Çarpma ve bölme işlemi hata verecektir. Bu maddede adı geçmeyen diğer operatörlerin test edilmesine gerek yoktur. Döndürülen hata şu olacaktır: "Hata: Operatör '+' veya '-' olmalıdır."
4. Liste Elemanı Her sayı (işlenen) yalnızca rakam içermelidir. Aksi halde fonksiyon şunu döndürür: 'Hata: Sayılar yalnızca rakam içermelidir.'
5. Liste Elemanı Her işlenenin (diğer bir deyişle operatörün her iki tarafındaki sayı) genişliği maksimum dört basamaktır. Aksi takdirde, döndürülen hata dizesi şöyle olacaktır: 'Hata: Sayılar dört basamaktan fazla olamaz.'
6. Liste Elemanı Kullanıcı doğru sorun biçimini sağladıysa, döndüreceğiniz dönüşüm şu kurallara uyacaktır:
Operatör ile iki işlenenden en uzun olanı arasında tek boşluk olmalıdır, operatör ikinci işlenenle aynı satırda olacaktır, her iki işlenen de belirtildiği gibi aynı sırada olacaktır (birincisi en üstteki olacak ve ikincisi alt kısım olacaktır).
7. Liste Elemanı Sayılar sağa hizalanmalıdır.
8. Liste Elemanı Her problem arasında dört boşluk olmalıdır.
9. Liste Elemanı Her problemin altında kısa çizgiler bulunmalıdır. Çizgiler her problemin tüm uzunluğu boyunca ayrı ayrı uzanmalıdır. (Yukarıdaki örnek bunun nasıl görünmesi gerektiğini gösterir.)
-Not: Testlerin daha ayrıntılı çıktısını görmek için tarayıcı konsolunu F12 ile açın.
