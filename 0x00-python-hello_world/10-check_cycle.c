#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: a list
 * Return: return 0 if there is no cycle
 *	   return 1 if there is cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	while (faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;


		if (slower == faster)
			return (1);
	}
	return (0);
}
