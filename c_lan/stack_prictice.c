#define basic 100
#define STACKINCREMENT 10
#include<stdio.h>
#include<stdlib.h>
typedef struct {
	int* base;
	int* top;
	int stacksize;
}SqStack;
int InitStack(SqStack S) {
	S.base = (int*)malloc(basic * sizeof(int));
	if (!S.base)exit(1);
	S.top = S.base;
	S.stacksize = basic;
	return 1;
}
int Gettop(SqStack S, int e) {
	if (S.top == S.base) return 0;
	e = *(S.top - 1);
	return e;
}
int Push(SqStack S, int e) {
	if (S.top - S.top >= S.stacksize) {
		S.base = (int*)realloc(S.base, (S.stacksize + STACKINCREMENT) * sizeof(int));
		if (!S.base)exit(1);
		S.top = S.base + S.stacksize;//为什么不能直接++
		S.stacksize += STACKINCREMENT;
	}
	*S.top++ = e;
	return 1;
}
int Pop(SqStack S, int e) {
	if (S.top == S.base)return 0;
	e = *--S.top;
	return e;
}
int main() {
	printf("1");
	// SqStack p;
	// int e=0;
	// InitStack(p);
	// printf("%d\n",p.base);
	// Push(p, 312);
	// printf("%d", p.top);
	// return 0;

}