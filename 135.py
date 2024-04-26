{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3e53256",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "outerloop:1\n",
      "innerloop:2\n",
      "nested loop ended\n",
      "innerloop:2\n",
      "nested loop ended\n",
      "outerloop:1\n",
      "innerloop:2\n",
      "nested loop ended\n",
      "innerloop:2\n",
      "nested loop ended\n",
      "outerloop:1\n",
      "innerloop:2\n",
      "nested loop ended\n",
      "innerloop:2\n",
      "nested loop ended\n"
     ]
    }
   ],
   "source": [
    "#nested while loop\n",
    "i=1\n",
    "while i<=3:\n",
    "    print(\"outerloop:1\")\n",
    "    i+=1\n",
    "    j=1\n",
    "    while j<=2:\n",
    "        print(\"innerloop:2\")\n",
    "        j+=1\n",
    "        print(\"nested loop ended\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e9a57a83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the sum of the 10 consecutive numbers starting from 1 is : 1\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 2\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 3\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 4\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 5\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 6\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 7\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 8\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 9\n",
      "the sum of the 10 consecutive numbers starting from 1 is : 10\n"
     ]
    }
   ],
   "source": [
    "#demonstrating 10 consecutive number starting from 1:\n",
    "Total=0\n",
    "for i in range(1,11):\n",
    "    Total+= 1\n",
    "    print(\"the sum of the 10 consecutive numbers starting from 1 is :\",i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9e341c3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "8\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "#overloading method\n",
    "class OverloadingDemo:\n",
    "    def add(self, a, b=0, c=0):\n",
    "        return a + b + c\n",
    "\n",
    "demo = OverloadingDemo()\n",
    "result1 = demo.add(5)\n",
    "result2 = demo.add(5, 3)\n",
    "result3 = demo.add(5, 3, 2)\n",
    "\n",
    "print(result1)\n",
    "print(result2)\n",
    "print(result3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21055608",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
