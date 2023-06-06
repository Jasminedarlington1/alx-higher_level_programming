#include "lists.h"
#include <stdio.h>

/**
 * check_cycle = function that checks if a singly list contains a cycle
 * @list: singly linked list
 *
 * Return: 0, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *p, *j;

	if (list == NULL || list->next == NULL)
		return (0);
	p = list->next;
	j = list->next->next;

	while (p && j && j->next)
	{
		if (p == j)
			return (1);

		p = p->next;
		j = j->next->next;
	}
	return (0);
}
