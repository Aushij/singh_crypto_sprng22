#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 256
void printBN(char *msg, BIGNUM * num1, BIGNUM * num2)
{
/* Use BN_bn2hex(a) for hex string
* Use BN_bn2dec(a) for decimal string */
char * number_str1 = BN_bn2hex(num1);
char * number_str2 = BN_bn2hex(num2);
printf("%s %s %s\n", msg, number_str1, number_str2);
OPENSSL_free(number_str1);
OPENSSL_free(number_str2);
}
int main ()
{
BN_CTX *ctx = BN_CTX_new();
BIGNUM *p = BN_new();
BIGNUM *q = BN_new();
BIGNUM *n = BN_new();
BIGNUM *phi = BN_new();
BIGNUM *e = BN_new();
BIGNUM *d = BN_new();
BIGNUM *res = BN_new();
BIGNUM *p_minus_1 = BN_new();
BIGNUM *q_minus_1 = BN_new();

BN_hex2bn(&p, "F7E75FDC469067FFDC4E847C51F452DF");
BN_hex2bn(&q, "E85CED54AF57E53E092113E62F436F4F");
BN_hex2bn(&e, "0D88C3");

BN_mul(n,p,q, ctx);
printBN("Public key= ",e,n);

BN_sub(p_minus_1,p,BN_value_one());
BN_sub(q_minus_1,q,BN_value_one());
BN_mul(phi,p_minus_1,q_minus_1,ctx);
BN_gcd(res,phi,e,ctx);

if(!BN_is_one(res))
{
printf("e and phi(n) are not relatively prime\n");
exit(0);
}
BN_mod_inverse(d, e, phi, ctx);
printBN("Private Key= ", d,n);

BN_clear_free(p);
BN_clear_free(q);
BN_clear_free(e);
BN_clear_free(d);
BN_clear_free(n);
BN_clear_free(res);
BN_clear_free(phi);
BN_clear_free(p_minus_1);
BN_clear_free(q_minus_1);
return 0;
}
