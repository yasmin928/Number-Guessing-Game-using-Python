{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f56f97d5",
   "metadata": {},
   "source": [
    "# Number Guessing Game using Python\n",
    "To create a guessing game, we need to write a program to select a random number between 1 and 10. To give hints to the user, we can use conditional statements to tell the user if the guessed number is smaller, greater than or equal to the randomly selected number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0da6e92c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#write a program to create a number guessing game using Python:\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e6eda5d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = random.randrange(1,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "605c7721",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any number: 2\n"
     ]
    }
   ],
   "source": [
    "guess = int(input(\"Enter any number: \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4e9d8b88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low\n",
      "Enter number again: 4\n",
      "Too low\n",
      "Enter number again: 5\n",
      "you guessed it right!!\n"
     ]
    }
   ],
   "source": [
    "while n!= guess:\n",
    "    if guess < n:\n",
    "        print(\"Too low\")\n",
    "        guess = int(input(\"Enter number again: \"))\n",
    "    elif guess > n:\n",
    "        print(\"Too high!\")\n",
    "        guess = int(input(\"Enter number again: \"))\n",
    "    else:\n",
    "      break\n",
    "print(\"you guessed it right!!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c429d09",
   "metadata": {},
   "source": [
    "#### If the guessed number is lower than the randomly selected number, the user will see “too low”. If the guessed number is higher than the randomly selected number, the user will see “too high”. When the user guesses the correct number, “you guessed it right!!” will be displayed in the output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "691475af",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
