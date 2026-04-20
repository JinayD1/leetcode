typedef struct {
    // dynamic array for stack storage
   int* stack;

   // length
   int top;

   // max num of ints
   int max; 

   // pointer to min int dynamic array
   int* min;

   // min stack top index
   int mintop;

    // max num of ints
   int minmax; 
} MinStack;


MinStack* minStackCreate() {
    MinStack* nstack = malloc(sizeof(MinStack));
    nstack->max = 1;
    nstack->stack = malloc(sizeof(int) * nstack->max);
    nstack->top = -1;

    nstack->minmax = 1;
    nstack->min = malloc(sizeof(int) * nstack->minmax);
    nstack->mintop = -1;
    return nstack;
}

void minStackPush(MinStack* obj, int val) {
    if (obj->max < (obj->top) + 2) {
        obj->stack = realloc(obj->stack, sizeof(int) * (2 * obj->max));
        obj->max *= 2; 
    }

    (obj->stack)[++(obj->top)] = val;

    if (obj->mintop == -1 || val <= (obj->min)[obj->mintop]) {
        if (obj->mintop + 2 > (obj->minmax)) {
            obj->min = realloc(obj->min, sizeof(int) * (2 * obj->minmax));
            obj->minmax *= 2; 
        }
        obj->min[++(obj->mintop)] = val; 
    }
}

void minStackPop(MinStack* obj) {
    if ((obj->stack)[obj->top] == (obj->min)[obj->mintop]) {
        obj->mintop--;
    }
    obj->top--;
}

int minStackTop(MinStack* obj) {
    return (obj->stack)[obj->top];
}

int minStackGetMin(MinStack* obj) {
    return obj->min[obj->mintop]; 
}

void minStackFree(MinStack* obj) {
    free(obj->min);
    free(obj->stack);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/